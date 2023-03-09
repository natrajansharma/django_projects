
from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
