from .models import Paciente
from .serializers import PacienteSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'matricula', 'cpf']
