from rest_framework import viewsets

from .serializers import CustomerInfoSerializer
from .models import CustomerInfo


class CustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all().order_by('name')
    serializer_class = CustomerInfoSerializer