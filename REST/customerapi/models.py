from django.db import models

class CustomerInfo(models.Model):
    name = models.CharField(max_length=60)
    model_selected = models.CharField(max_length=60)
    contactnumber = models.IntegerField()
    emailid = models.EmailField(max_length=50)
    booktime = models.DateTimeField()
