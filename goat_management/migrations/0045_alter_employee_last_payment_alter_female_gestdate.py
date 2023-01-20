# Generated by Django 4.1.1 on 2023-01-20 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goat_management", "0044_alter_female_gestdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="last_payment",
            field=models.DateField(
                blank=True, default=datetime.date(2023, 1, 20), null=True
            ),
        ),
        migrations.AlterField(
            model_name="female",
            name="gestdate",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2023, 1, 20, 17, 5, 28, 897280),
                null=True,
            ),
        ),
    ]