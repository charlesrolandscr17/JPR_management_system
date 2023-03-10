# Generated by Django 4.1.1 on 2023-01-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ambition",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(max_length=255)),
                ("dueDate", models.DateTimeField()),
                ("uploadDate", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("complete", models.BooleanField(default=False)),
            ],
        ),
    ]
