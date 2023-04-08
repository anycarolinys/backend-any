# from rest_framework import serializers
# from .models import Circunstancia

# class CircunstanciaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Circunstancia
#         fields = '__all__'
#         # fields = ['id','circunstancia']

from rest_framework import serializers
from .models import Circunstancia
from formularios.formAFM.models import FormAFM


class CircunstanciaSerializer(serializers.ModelSerializer):
    # formAFM = serializers.PrimaryKeyRelatedField(queryset=FormAFM.objects.all())

    class Meta:
        model = Circunstancia
        # fields = '__all__'
        fields = ['id', 'circunstancia']
        write_only_fields = ['formAFM']

    # def create(self, validated_data):
    #     formafm_id = validated_data.pop('formAFM')
    #     formAFM = FormAFM.objects.get(id=formafm_id)
    #     circunstancia = Circunstancia.objects.create(formAFM=formAFM, **validated_data)
    #     return circunstancia