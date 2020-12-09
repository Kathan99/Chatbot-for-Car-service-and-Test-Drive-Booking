from rest_framework import viewsets


from .serializers import CarInfoSerializer
from .models import CarInfo


class CarInfoViewSet(viewsets.ModelViewSet):
    lookup_field = "name"
    queryset = CarInfo.objects.all().order_by('name')
    serializer_class = CarInfoSerializer
