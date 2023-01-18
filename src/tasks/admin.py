from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    """
    Django model admin to represent Task model.
    """
    list_display = ['description', 'is_done', 'user', 'priority',]
