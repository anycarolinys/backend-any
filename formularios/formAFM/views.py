from .models import FormAFM
from .serializers import FormAFMSerializer
from rest_framework import  viewsets,generics

# class FormAFMViewSet(viewsets.ModelViewSet):
#     queryset = FormAFM.objects.all()
#     serializer_class = FormAFMSerializer

class FormAFMListCreateView(generics.ListCreateAPIView):
    queryset = FormAFM.objects.all()
    serializer_class = FormAFMSerializer

class FormAFMRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormAFM.objects.all()
    serializer_class = FormAFMSerializer