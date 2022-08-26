# Generated by Django 4.1 on 2022-08-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0002_alter_contract_is_directors_approval_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="is_directors_approval",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="contract",
            name="is_ooc",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="historicalcontract",
            name="is_directors_approval",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="historicalcontract",
            name="is_ooc",
            field=models.BooleanField(default=False),
        ),
    ]