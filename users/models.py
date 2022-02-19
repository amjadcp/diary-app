from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=False)
    email = models.EmailField(_('email address'), unique=True)
    birthday = models.DateField(default='2002-08-10')
    gender = models.CharField(max_length=7, choices=choices)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'