# Generated by Django 5.0.6 on 2024-05-31 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
        ("expense", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="account",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.account",
            ),
        ),
    ]