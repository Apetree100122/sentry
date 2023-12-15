from __future__ import annotations

from typing import Any, Mapping

from sentry import features
from sentry.integrations.slack.message_builder import SlackBody
from sentry.integrations.slack.message_builder.base.block import BlockSlackMessageBuilder
from sentry.integrations.slack.utils.escape import escape_slack_text
from sentry.notifications.notifications.base import BaseNotification
from sentry.services.hybrid_cloud.actor import RpcActor
from sentry.types.integrations import ExternalProviders
from sentry.utils import json


class SlackNotificationsMessageBuilder(BlockSlackMessageBuilder):
    def __init__(
        self,
        notification: BaseNotification,
        context: Mapping[str, Any],
        recipient: RpcActor,
    ) -> None:
        super().__init__()
        self.notification = notification
        self.context = context
        self.recipient = recipient

    def build(self) -> SlackBody:
        # print("SlackNotificationsMessageBuilder")
        callback_id_raw = self.notification.get_callback_data()
        if features.has("organizations:slack-block-kit", self.notification.organization):
            title_link = self.notification.get_title_link(self.recipient, ExternalProviders.SLACK)
            text = (
                self.notification.get_message_description(self.recipient, ExternalProviders.SLACK),
            )
            footer = self.notification.build_notification_footer(
                self.recipient, ExternalProviders.SLACK
            )
            blocks = [
                self.get_markdown_block(
                    text=f"<{title_link}|*{escape_slack_text(self.notification.build_attachment_title(self.recipient))}*>  \n{text}",
                )
            ]
            blocks.append(self.get_context_block(text=footer))
            return self._build_blocks(
                *blocks,
                fallback_text=text,
                # callback_id=json.dumps(callback_id_raw) if callback_id_raw else None
            )
        return self._build(
            title=self.notification.build_attachment_title(self.recipient),
            title_link=self.notification.get_title_link(self.recipient, ExternalProviders.SLACK),
            text=self.notification.get_message_description(self.recipient, ExternalProviders.SLACK),
            footer=self.notification.build_notification_footer(
                self.recipient, ExternalProviders.SLACK
            ),
            actions=self.notification.get_message_actions(self.recipient, ExternalProviders.SLACK),
            callback_id=json.dumps(callback_id_raw) if callback_id_raw else None,
        )
