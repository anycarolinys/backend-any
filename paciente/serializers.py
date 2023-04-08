from rest_framework import serializers
from .models import Paciente
from projetoinca.validators import *

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        read_only_fields = ('imc',)

    def calculo_imc(self, data):
        return round(data['peso'] / (data['altura'] * data['altura']), 2)
    
    def create(self, validated_data):
        imc = self.calculo_imc(validated_data)
        
        return Paciente.objects.create(imc=imc, **validated_data)

    def validate(self, data):
        matricula_valida(data['matricula'])
        nome_valido(data['nome'])
        data_nascimento_valida(data['data_nascimento'])
        cpf_valido(data['cpf'])
        return data
