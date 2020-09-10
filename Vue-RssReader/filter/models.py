from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)

class Snippet(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name