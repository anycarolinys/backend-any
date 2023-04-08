from django.db import models
# from circunstancia.models import Circunstancia
from consulta.models import Consulta

# class CircunstanciaChoice(Enum):
#     T  = 'Tosse'
#     E = 'Espirro'
#     A = 'Andar '
#     R = 'Riso'
#     P = 'Pular'
#     PP = 'Pegar peso'
#     RS = 'Relação sexual'

# class CustomReadableValueEnumModel(models.Model):
#     enumerated_field = EnumChoiceField(
#         Circunstancia,
#         choice_builder=attribute_value
#     )

SIM_NAO = [('Sim', 'Sim'), ('Não', 'Não')]
# CIRCUNSTANCIA = [('Tosse', 'Tosse'), ('Espirro', 'Espirro'),
                # ('Andar', 'Andar'), ('Riso', 'Riso'), ('Pular', 'Pular'), ('Pegar peso', 'Pegar peso'), ('Relação sexual', 'Relação sexual')]
INTENSIDADE_PERDA = [('Muita', 'Muita'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca')]
QUANTIDADE_PERDA = [('Gota', 'Gota'), ('Colher', 'Colher'), ('Jato', 'Jato')]
TIPO_INCONTINENCIA = [('Urgência', 'Urgência'), ('Esforço', 'Esforço'), 
                      ('Mista', 'Mista'), ('Transbordamento', 'Transbordamento')]
TOQUE_VAGINAL= [('Unidigital', 'Unidigital'), ('Bidigital', 'Bidigital')]
DOR = [('Ausente', 'Ausente'), ('Suave', 'Suave'), ('Severo', 'Severo')]
MUSCULATURA_ACESSORIA = [('Abdômen', 'Abdômen'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')]
ATIVIDADE_TONICA = [('Diminuído', 'Diminuído'), ('Normal','Normal'), ('Aumentado', 'Aumentado')]
FORCA_MUSCULATURA = [('0', 'Ausência de resposta muscular'),
                    ('1', 'Esboço de contração não sustentada'),
                    ('2', 'Presença de contração de pequena intensidade, mas que se sustenta'),
                    ('3', 'Contração moderada, sentida com o aumento da pressão intavaginal, que comprime os dedos do examinador com pequena elevação cranial da parede vaginal'),
                    ('4', 'Contração satisfatória, que aperta os dedos do examinador, com elevação da parede vaginal em direção à sínfise púbica'),
                    ('5', 'Contração forte, compressão firme dos dedos do examinador com movimento positivo em relação à sínfise púbica')]
ESCALA_NEW_PERFECT = [('P', 'Power'),
                    ('E', 'Endurance'),
                    ('R', 'Repetition'),
                    ('F', 'Fast')]


class FormAFM(models.Model):
    # AFM06 = EnumChoiceField(Circunstancia, choice_builder=attribute_value)
    # AFM06 = models.CharField(max_length=20, choices=[(c, c.value) for c in CircunstanciaChoice], verbose_name='Circunstância da perda:', null=True)
    # AFM06 = EnumField(choices=CircunstanciaChoice, to_choice=lambda x: (x.value, x.name), to_repr=lambda x: x.value)
    # AFM06 = models.ManyToManyField(Circunstancia)
    # AFM06 = models.CharField(max_length=20, verbose_name='Circunstância da perda:', null=True)

    AFM01 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Bebe 2 litros de água?')
    AFM02  = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sente vontade de urinar?')
    AFM03 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Tem sensação de esvaziamento incompleto?')
    AFM04 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Há gotejamento após esvaziament')
    AFM05 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Você perde xixi?')
    AFM07 = models.DateField(verbose_name='Data do último episódio:', null=True)
    AFM08 = models.IntegerField(verbose_name='Perda diária:', null=True)
    AFM09 = models.CharField(max_length=20, choices=INTENSIDADE_PERDA, verbose_name='Intensidade de perda:', null=True)
    AFM10 = models.CharField(max_length=20, choices=QUANTIDADE_PERDA, verbose_name='Quantidade da perda:', null=True)
    AFM11 = models.CharField(max_length=20, choices=TIPO_INCONTINENCIA, verbose_name='Tipo da incontinência urinária:', null=True)
    AFM12 = models.DateField(verbose_name='Início dos sintomas:', null=True)
    AFM13 = models.IntegerField(verbose_name='Frequência urinária diária:')
    AFM14 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Dor para urinar?')
    AFM15 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Infecção urinária?')
    AFM16 = models.IntegerField(verbose_name='Quantas vezes?', null=True)
    AFM17 = models.DateField(verbose_name='Qual a data do último episódio?', null=True)
    AFM18 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name=' Uso de forro?')
    AFM19 = models.IntegerField(verbose_name='Quantidade por dia?', null=True)
    AFM20 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name=' Enurese?')
    AFM21 = models.IntegerField(verbose_name='Quantidade de vezes?', null=True)
    AFM22 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Nocturia?')
    AFM23 = models.IntegerField(verbose_name='Quantidade de vezes?', null=True)
    AFM24 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sente protuberância ou algo caindo que pode ver ou sentir na área vaginal?')
    AFM25 = models.CharField(max_length=20, choices=TOQUE_VAGINAL, verbose_name='Toque vaginal')
    AFM26 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Desconforto ao toque vaginal?')
    AFM27 = models.CharField(max_length=20, choices=DOR, verbose_name='Dor')
    AFM28 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Sangramento Vaginal')
    AFM29 = models.FloatField(verbose_name='Comprimento')
    AFM30 = models.IntegerField(verbose_name='Segundos de contração do MAP sustentada')
    AFM31 = models.IntegerField(verbose_name='Contrações rápidas sem perder a força')
    AFM32= models.CharField(max_length=3, choices=SIM_NAO,  verbose_name='Usa musculatura acessória para contração?')
    AFM33= models.CharField(max_length=20, choices=MUSCULATURA_ACESSORIA, verbose_name='Musculatura: ')
    AFM34= models.CharField(max_length=20, choices=ATIVIDADE_TONICA, verbose_name='Atividade tônica dos músculos do assoalho pélvico')
    AFM35 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Contração do levantador do ânus/ contração em direção à sínfise púbica')
    AFM36 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Exercícios com dilatadores')
    AFM37 = models.IntegerField(verbose_name='Frequência dilatadores', null=True)
    AFM38 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Relação sexual')
    AFM39 = models.IntegerField(verbose_name='Frequência relação sexual', null=True)
    AFM40 = models.CharField(max_length=3, choices=SIM_NAO, verbose_name='Desconforto na relação sexual?', null=True)
    AFM41 = models.CharField(max_length=20, choices=FORCA_MUSCULATURA, verbose_name='Força da musculatura do assoalho pélvico')
    AFM42 = models.CharField(max_length=20, choices=ESCALA_NEW_PERFECT, verbose_name='Escala New Perfect')
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.consulta)