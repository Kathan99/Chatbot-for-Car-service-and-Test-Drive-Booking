from rest_framework import serializers

from .models import CustomerInfo

class CustomerInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = ('name', 'model_selected', 'contactnumber', 'emailid', 'booktime')