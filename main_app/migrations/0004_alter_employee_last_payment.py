# Generated by Django 4.1.1 on 2022-10-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_employee_last_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_payment',
            field=models.DateField(blank=True, null=True),
        ),
    ]