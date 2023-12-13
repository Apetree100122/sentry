import logging
from datetime import datetime, timezone
from typing import Any, Mapping, Optional, cast

from arroyo.backends.kafka import KafkaPayload
from arroyo.processing.strategies import (
    CommitOffsets,
    ProcessingStrategy,
    ProcessingStrategyFactory,
)
from arroyo.types import Commit, Message, Partition
from django.core.cache import cache
from django.db.models import F
from sentry_kafka_schemas.schema_types.snuba_generic_metrics_v1 import GenericMetric

from sentry.constants import DataCategory
from sentry.models.project import Project
from sentry.sentry_metrics.indexer.strings import SHARED_TAG_STRINGS, TRANSACTION_METRICS_NAMES
from sentry.sentry_metrics.use_case_id_registry import UseCaseID
from sentry.sentry_metrics.utils import reverse_resolve_tag_value
from sentry.snuba.metrics import parse_mri
from sentry.snuba.metrics.naming_layer.mri import is_custom_metric
from sentry.utils import json, metrics
from sentry.utils.outcomes import Outcome, track_outcome

logger = logging.getLogger(__name__)

# 7 days of TTL.
CACHE_TTL_IN_SECONDS = 60 * 60 * 24 * 7


def _get_project_flag_updated_cache_key(org_id: int, project_id: int) -> str:
    return f"has-custom-metrics-flag-updated:{org_id}:{project_id}"


def _mark_flag_as_updated(org_id: int, project_id: int):
    cache_key = _get_project_flag_updated_cache_key(org_id, project_id)
    cache.set(cache_key, "1", CACHE_TTL_IN_SECONDS)


def _was_flag_updated(org_id: int, project_id: int) -> bool:
    cache_key = _get_project_flag_updated_cache_key(org_id, project_id)
    return cache.get(cache_key) is not None


class BillingMetricsConsumerStrategyFactory(ProcessingStrategyFactory[KafkaPayload]):
    def create_with_partitions(
        self,
        commit: Commit,
        partitions: Mapping[Partition, int],
    ) -> ProcessingStrategy[KafkaPayload]:
        return BillingTxCountMetricConsumerStrategy(CommitOffsets(commit))


class BillingTxCountMetricConsumerStrategy(ProcessingStrategy[KafkaPayload]):
    """A metrics consumer that generates a billing outcome for each processed
    transaction, processing a bucket at a time. The transaction count is
    directly taken from the `c:transactions/usage@none` counter metric.
    """

    #: The ID of the metric used to count transactions
    metric_id = TRANSACTION_METRICS_NAMES["c:transactions/usage@none"]
    profile_tag_key = str(SHARED_TAG_STRINGS["has_profile"])

    def __init__(self, next_step: ProcessingStrategy[Any]) -> None:
        self.__next_step = next_step
        self.__closed = False

    def poll(self) -> None:
        self.__next_step.poll()

    def terminate(self) -> None:
        self.close()

    def close(self) -> None:
        self.__closed = True
        self.__next_step.close()

    def submit(self, message: Message[KafkaPayload]) -> None:
        assert not self.__closed

        payload = self._get_payload(message)

        self._produce_billing_outcomes(payload)
        self._flag_metric_received_for_project(payload)

        self.__next_step.submit(message)

    def _get_payload(self, message: Message[KafkaPayload]) -> GenericMetric:
        payload = json.loads(message.payload.value.decode("utf-8"), use_rapid_json=True)
        return cast(GenericMetric, payload)

    def _count_processed_items(self, generic_metric: GenericMetric) -> Mapping[DataCategory, int]:
        if generic_metric["metric_id"] != self.metric_id:
            return {}
        value = generic_metric["value"]
        try:
            quantity = max(int(value), 0)
        except TypeError:
            # Unexpected value type for this metric ID, skip.
            return {}

        items = {DataCategory.TRANSACTION: quantity}

        if self._has_profile(generic_metric):
            # The bucket is tagged with the "has_profile" tag,
            # so we also count the quantity of this bucket towards profiles.
            # This assumes a "1 to 0..1" relationship between transactions and profiles.
            items[DataCategory.PROFILE] = quantity

        return items

    def _has_profile(self, generic_metric: GenericMetric) -> bool:
        return bool(
            (tag_value := generic_metric["tags"].get(self.profile_tag_key))
            and "true"
            == reverse_resolve_tag_value(
                UseCaseID.TRANSACTIONS, generic_metric["org_id"], tag_value
            )
        )

    def _produce_billing_outcomes(self, generic_metric: GenericMetric) -> None:
        for category, quantity in self._count_processed_items(generic_metric).items():
            self._produce_billing_outcome(
                org_id=generic_metric["org_id"],
                project_id=generic_metric["project_id"],
                category=category,
                quantity=quantity,
            )

    def _produce_billing_outcome(
        self, *, org_id: int, project_id: int, category: DataCategory, quantity: int
    ) -> None:
        if quantity < 1:
            return

        # track_outcome does not guarantee to deliver the outcome, making this
        # an at-most-once delivery.
        #
        # If it turns out that we drop too many outcomes on shutdown,
        # we may have to revisit this part to achieve a
        # better approximation of exactly-once delivery.
        track_outcome(
            org_id=org_id,
            project_id=project_id,
            key_id=None,
            outcome=Outcome.ACCEPTED,
            reason=None,
            timestamp=datetime.now(timezone.utc),
            event_id=None,
            category=category,
            quantity=quantity,
        )

    def _flag_metric_received_for_project(self, generic_metric: GenericMetric) -> None:
        try:
            org_id = generic_metric["org_id"]
            project_id = generic_metric["project_id"]
            if _was_flag_updated(org_id, project_id):
                metrics.incr("ddm.consumer.project_loading.debounced")
                return None

            project = Project.objects.get_from_cache(id=project_id)
            metrics.incr("ddm.consumer.project_loading.loaded_from_cache")

            if not project.flags.has_custom_metrics:
                metrics.incr("ddm.consumer.project_loading.flag_not_set")

                # We try to extract the MRI from the metric_id since our goal is to check whether the MRI belongs to
                # a metric in the `custom` namespace.
                metric_mri = self._resolve(
                    generic_metric["mapping_meta"], generic_metric["metric_id"]
                )
                parsed_mri = parse_mri(metric_mri)
                if parsed_mri is None or not is_custom_metric(parsed_mri):
                    return None

                # We assume that the flag update is reflected in the cache, so that upcoming calls will get the up-to-
                # date project with the `has_custom_metrics` flag set to true.
                project.update(flags=F("flags").bitor(Project.flags.has_custom_metrics))

                _mark_flag_as_updated(org_id, project_id)
            else:
                _mark_flag_as_updated(org_id, project_id)
        except Project.DoesNotExist:
            pass

        return None

    def _resolve(self, mapping_meta: Mapping[str, Any], indexed_value: int) -> Optional[str]:
        for _, inner_meta in mapping_meta.items():
            if (string_value := inner_meta.get(str(indexed_value))) is not None:
                return string_value

        return None

    def join(self, timeout: Optional[float] = None) -> None:
        self.__next_step.join(timeout)
