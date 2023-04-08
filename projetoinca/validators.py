from rest_framework import serializers
from validate_docbr import CNPJ, CPF
from django.utils import timezone


def cpf_valido(cpf):
    if len(cpf) != 11:
            raise serializers.ValidationError({'cpf':'104'})
        
    numero_cpf = CPF()
    if not numero_cpf.validate(cpf):
        raise serializers.ValidationError({'cpf': '105'})
    return cpf
    
def cnpj_valido(cnpj):
        if len(cnpj) != 14:
            raise serializers.ValidationError({'cnpj':'106'})
        
        numero_cnpj = CNPJ()
        if not numero_cnpj.validate(cnpj):
            raise serializers.ValidationError({'cnpj': '107'})
        return cnpj

def matricula_valida(matricula):
    if len(matricula) != 6:
        raise serializers.ValidationError({'matricula':'108'})
    return matricula

def nome_valido(nome):
    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome):
        raise serializers.ValidationError({'nome':'109'})
    return nome

def data_valida(data_retorno):
    if data_retorno is not None:
        if timezone.now().date() > data_retorno:
            raise serializers.ValidationError({'data_retorno':'110'})
        return data_retorno

def data_nascimento_valida(data_nascimento):
    if data_nascimento is not None:
        if data_nascimento > timezone.now().date():
            raise serializers.ValidationError({'data_nascimento':'111'})
        return data_nascimento
