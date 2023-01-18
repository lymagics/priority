from django.conf import settings
from django.db import models


class Task(models.Model):
    """
    Django ORM model to represent 'tasks' table.
    """
    class Priority(models.TextChoices):
        HIGH = 'H', 'High'
        MEDIUM = 'M', 'Medium'
        LOW = 'L', 'Low'

    description = models.CharField(max_length=280)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=Priority.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
