from rest_framework import serializers
from .models import Instituicao
from projetoinca.validators import *

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'

    def validate(self, data):

        cnpj_valido(data['cnpj'])
        nome_valido(data['nome'])
        
        return data
