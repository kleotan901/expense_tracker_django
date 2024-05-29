# Generated by Django 5.0.6 on 2024-05-29 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
        ("expense", "0003_alter_expense_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="currency",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="account_currency",
                to="account.account",
            ),
        ),
    ]