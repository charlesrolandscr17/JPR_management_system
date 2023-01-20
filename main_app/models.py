from django.db import models


# Create your models here.
class Ambition(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(max_length=255)
    dueDate = models.DateTimeField(auto_now=False)
    uploadDate = models.DateField(auto_now=True)


class Todo(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    complete = models.BooleanField(default=False)
