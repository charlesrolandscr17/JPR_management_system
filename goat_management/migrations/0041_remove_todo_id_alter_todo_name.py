# Generated by Django 4.1.1 on 2022-11-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goat_management", "0040_todo_complete"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="id",
        ),
        migrations.AlterField(
            model_name="todo",
            name="name",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]