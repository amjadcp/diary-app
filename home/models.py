from turtle import title
from django.db import models
from users.models import User
# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
