# Generated by Django 3.2.23 on 2023-12-22 18:42

from django.db import migrations

import bitfield.models
from sentry.new_migrations.migrations import CheckedMigration


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production. For
    # the most part, this should only be used for operations where it's safe to run the migration
    # after your code has deployed. So this should not be used for most operations that alter the
    # schema of a table.
    # Here are some things that make sense to mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that they can
    #   be monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   have ops run this and not block the deploy. Note that while adding an index is a schema
    #   change, it's completely safe to run the operation after the code has deployed.
    is_dangerous = False

    dependencies = [
        ("sentry", "0625_change_rule_label_type_to_char256"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="flags",
            field=bitfield.models.BitField(
                [
                    "allow_joinleave",
                    "enhanced_privacy",
                    "disable_shared_issues",
                    "early_adopter",
                    "require_2fa",
                    "disable_new_visibility_features",
                    "require_email_verification",
                    "codecov_access",
                    "allow_member_project_creation",
                ],
                default=1,
            ),
        ),
    ]
