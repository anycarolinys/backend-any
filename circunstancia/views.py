from .models import Circunstancia
from .serializers import CircunstanciaSerializer
from rest_framework import viewsets, generics

# class CircunstanciaViewSet(viewsets.ModelViewSet):
#     queryset = Circunstancia.objects.all()
#     serializer_class = CircunstanciaSerializer

class CircunstanciaListCreateView(generics.ListCreateAPIView):
    queryset = Circunstancia.objects.all()
    serializer_class = CircunstanciaSerializer

class CircunstanciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Circunstancia.objects.all()
    serializer_class = CircunstanciaSerializer