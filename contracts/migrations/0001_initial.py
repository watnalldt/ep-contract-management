# Generated by Django 4.1 on 2022-08-23 09:39

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("clients", "0001_initial"),
        ("utilities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalContract",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "company_reg_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("site_name", models.CharField(max_length=255)),
                ("site_address", models.CharField(max_length=255)),
                (
                    "meter_serial_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("top_line", models.CharField(max_length=30)),
                ("mpan_mpr", models.CharField(max_length=255)),
                ("contract_end_date", models.DateField(blank=True, null=True)),
                ("is_ooc", models.BooleanField(default=False)),
                ("is_directors_approval", models.BooleanField(default=False)),
                ("eac", models.CharField(max_length=30)),
                ("vat", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "smart_meter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="clients.client",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="utilities.supplier",
                    ),
                ),
                (
                    "utility",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="utilities.utility",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Client Contract",
                "verbose_name_plural": "historical Client Contracts",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "company_reg_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("site_name", models.CharField(max_length=255)),
                ("site_address", models.CharField(max_length=255)),
                (
                    "meter_serial_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("top_line", models.CharField(max_length=30)),
                ("mpan_mpr", models.CharField(max_length=255)),
                ("contract_end_date", models.DateField(blank=True, null=True)),
                ("is_ooc", models.BooleanField(default=False)),
                ("is_directors_approval", models.BooleanField(default=False)),
                ("eac", models.CharField(max_length=30)),
                ("vat", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "smart_meter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_contracts",
                        to="clients.client",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contract_suppliers",
                        to="utilities.supplier",
                    ),
                ),
                (
                    "utility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contract_utilities",
                        to="utilities.utility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Contract",
                "verbose_name_plural": "Client Contracts",
                "ordering": ["contract_end_date"],
            },
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["mpan_mpr"], name="contracts_c_mpan_mp_da9aba_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.UniqueConstraint(
                fields=("mpan_mpr", "contract_end_date"), name="unique_contract"
            ),
        ),
    ]