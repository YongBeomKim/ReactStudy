from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')

class People(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)