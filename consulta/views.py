from .models import Consulta
from .serializers import ConsultaSerializer
from rest_framework import viewsets


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
