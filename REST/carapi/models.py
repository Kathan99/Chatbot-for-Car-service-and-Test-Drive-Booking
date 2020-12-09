from django.db import models


class CarInfo(models.Model):
    name = models.CharField(max_length=60)
    price = models.CharField(max_length=60,blank=True,null=True)
    type = models.CharField(max_length=60)
    mileage = models.CharField(max_length=30)
    fueltype = models.CharField(max_length=10)
    transmission = models.CharField(max_length=10)
