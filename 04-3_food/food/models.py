from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    pImage = models.URLField()

    def __str__(self):
        return self.name


class Buger(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    pImage = models.URLField()

    def __str__(self):
        return self.name
