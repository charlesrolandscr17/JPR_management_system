# Generated by Django 4.1.1 on 2022-11-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("goat_management", "0033_rename_deworming_dewormer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="f_name",
            new_name="name",
        ),
    ]
