from django.db import models

from django.contrib.auth.models import AbstractUser
# from SuperB.utils.base import BaseModel

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# class User(AbstractUser):
#     password = models.CharField(max_length=500)

