# Generated by Django 4.1.1 on 2022-11-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goat_management", "0023_mdead_dod"),
    ]

    operations = [
        migrations.AddField(
            model_name="fdead",
            name="DoD",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
