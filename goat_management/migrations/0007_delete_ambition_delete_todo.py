# Generated by Django 4.1.1 on 2022-10-14 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goat_management', '0006_alter_todo_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ambition',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]