import hashlib

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Django ORM model to represent 'users' table.
    """
    about_me = models.TextField(default='')

    @property
    def avatar_url(self):
        """
        Property for accessing user avatar url.
        """
        email_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{email_hash}'
