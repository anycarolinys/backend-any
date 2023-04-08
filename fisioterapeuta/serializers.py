from rest_framework import serializers
from .models import Fisioterapeuta
from projetoinca.validators import *

class FisioterapeutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisioterapeuta
        fields = '__all__'
    
    def validate(self, data):
        matricula_valida(data['matricula'])
        nome_valido(data['nome'])

        return data
