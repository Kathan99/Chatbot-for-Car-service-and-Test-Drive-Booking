from django.db import models

# Create your models here.
class Customer(models.Model):


    name = models.CharField(max_length=60)
    customernumber = models.IntegerField(null=True)
    emailid = models.EmailField(max_length=60,null=True)
    model = models.CharField(max_length=60)
    fueltype = models.CharField(max_length=60)
    servicetype = models.CharField(max_length=60,blank=True)
    timeslot = models.DateTimeField()