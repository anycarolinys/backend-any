from .models import Administrador
from .serializers import AdministradorSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['login']
    search_fields = ['login']
