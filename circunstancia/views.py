from .models import Circunstancia
from .serializers import CircunstanciaSerializer
from rest_framework import viewsets

class CircunstanciaViewSet(viewsets.ModelViewSet):
    queryset = Circunstancia.objects.all()
    serializer_class = CircunstanciaSerializer