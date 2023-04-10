from .models import FormAFM
from .serializers import FormAFMSerializer
from rest_framework import  viewsets

class FormAFMViewSet(viewsets.ModelViewSet):
    queryset = FormAFM.objects.all()
    serializer_class = FormAFMSerializer