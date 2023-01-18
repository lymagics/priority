from django.contrib import admin

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    """
    Django model admin to represent User model.
    """
    list_display = ['pk', 'username', 'email']
