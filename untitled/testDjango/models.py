from __future__ import unicode_literals
from django.db import models

# create model and sync database tables

class Book(models.Model):
    name = models.CharField(max_length=100)
    userId = models.CharField(max_length=100)

class User(models.Model):
    userId = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)






