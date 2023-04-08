from .models import Fisioterapeuta
from .serializers import FisioterapeutaSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class FisioterapeutaViewSet(viewsets.ModelViewSet):
    queryset = Fisioterapeuta.objects.all()
    serializer_class = FisioterapeutaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'sobrenome', 'matricula']

class FisioterapeutasPorInstituicaoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FisioterapeutaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','matricula']

    def get_queryset(self):
        instituicao_id = self.kwargs['instituicao_id']
        return Fisioterapeuta.objects.filter(instituicao = instituicao_id)
