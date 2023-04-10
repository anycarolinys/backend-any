from rest_framework import serializers
from .models import Circunstancia

class CircunstanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circunstancia
        fields = ('id', 'circunstancia')