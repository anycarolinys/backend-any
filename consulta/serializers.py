from rest_framework import serializers
from .models import Consulta
from projetoinca.validators import *

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
    
    def validate(self, data):
        data_valida(data['data_retorno'])
        return data
