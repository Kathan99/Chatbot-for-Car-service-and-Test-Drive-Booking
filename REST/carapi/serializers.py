from rest_framework import serializers

from .models import CarInfo

class CarInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarInfo
        fields = ('name','price','type', 'mileage', 'fueltype', 'transmission')