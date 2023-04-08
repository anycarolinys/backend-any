from .models import Instituicao
from .serializers import InstituicaoSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cnpj']
