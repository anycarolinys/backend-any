from rest_framework import serializers

from ..funcoes import attempt_json_deserialize
from circunstancia.serializers import CircunstanciaSerializer
from circunstancia.models import Circunstancia
from consulta.serializers import ConsultaSerializer
from .models import FormAFM


class FormAFMSerializer(serializers.ModelSerializer):
    AFM06 = CircunstanciaSerializer(read_only=True, many=True)
    consulta = ConsultaSerializer(read_only=True)
    
    class Meta:
        model = FormAFM
        fields = ('id',
                'AFM01',
                'AFM02',
                'AFM03',
                'AFM04',
                'AFM05',
                'AFM06',
                'AFM07',
                'AFM08',
                'AFM09',
                'AFM10',
                'AFM11',
                'AFM12',
                'AFM13',
                'AFM14',
                'AFM15',
                'AFM16',
                'AFM17',
                'AFM18',
                'AFM19',
                'AFM20',
                'AFM21',
                'AFM22',
                'AFM23',
                'AFM24',
                'AFM25',
                'AFM26',
                'AFM27',
                'AFM28',
                'AFM29',
                'AFM30',
                'AFM31',
                'AFM32',
                'AFM33',
                'AFM34',
                'AFM35',
                'AFM36',
                'AFM37',
                'AFM38',
                'AFM39',
                'AFM40',
                'AFM41',
                'AFM42',
                'consulta')
    
    def create(self, validated_data):
        request = self.context['request']

        AFM06_data = request.data.get('AFM06')
        AFM06_data = attempt_json_deserialize(AFM06_data, expect_type=list)
        AFM06_objs = [Circunstancia.objects.create(**data) for data in AFM06_data]
        validated_data['AFM06'] = AFM06_objs

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().create(validated_data)

        return instance
    
    def update(self, instance, validated_data):
        request = self.context['request']

        AFM06_data = request.data.get('AFM06')
        validated_data['AFM06_id'] = AFM06_data

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().update(instance, validated_data)
        return instance