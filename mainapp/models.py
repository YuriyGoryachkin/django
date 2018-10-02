from django.db import models
from django.contrib.auth.models import AbstractUser

class UserMessenger(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=0)
