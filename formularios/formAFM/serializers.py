from rest_framework import serializers
from .models import FormAFM
from circunstancia.serializers import CircunstanciaSerializer
from circunstancia.models import Circunstancia

class FormAFMSerializer(serializers.ModelSerializer):
    AFM06 = CircunstanciaSerializer(many=True)
    # formAFM = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FormAFM
        # fields = '__all__'
        fields = ['id',
                'AFM01',
                'AFM02',
                'AFM03',
                'AFM04',
                'AFM05',
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
                'consulta',
                'AFM06']
    
    # def create(self, validated_data):
    #     resposta = validated_data.pop('AFM06', [])
    #     formafm = FormAFM.objects.create(**validated_data)
    #     for r in resposta:
    #         Circunstancia.objects.create(pergunta=formafm, **r)
    #     return formafm
    
    # def update(self, instance, validated_data):
    #     respostas_data = validated_data.pop('respostas', [])
    #     instance.texto = validated_data.get('texto', instance.texto)
    #     instance.save()
    #     for resposta_data in respostas_data:
    #         resposta_id = resposta_data.get('id', None)
    #         if resposta_id:
    #             resposta = Circunstancia.objects.get(id=resposta_id)
    #             resposta.texto = resposta_data.get('texto', resposta.texto)
    #             resposta.save()
    #         else:
    #             Circunstancia.objects.create(pergunta=instance, **resposta_data)
    #     return instance
    
    
    def create(self, validated_data):
        circunstancias_data = validated_data.pop('AFM06')
        formafm = FormAFM.objects.create(**validated_data)

        for circunstancia_data in circunstancias_data:
            FormAFM.objects.create(formafm=formafm, **circunstancia_data)
        
        return formafm