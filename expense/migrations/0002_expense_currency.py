# Generated by Django 5.0.6 on 2024-05-29 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
        ("expense", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="currency",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="account",
                to="account.account",
            ),
        ),
    ]
