# Generated by Django 4.1.7 on 2023-04-05 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consulta', '0002_alter_consulta_data_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormAFM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AFM01', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Bebe 2 litros de água?')),
                ('AFM02', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sente vontade de urinar?')),
                ('AFM03', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Tem sensação de esvaziamento incompleto?')),
                ('AFM04', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Há gotejamento após esvaziament')),
                ('AFM05', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Você perde xixi?')),
                ('AFM07', models.DateField(null=True, verbose_name='Data do último episódio:')),
                ('AFM08', models.IntegerField(null=True, verbose_name='Perda diária:')),
                ('AFM09', models.CharField(choices=[('Muita', 'Muita'), ('Moderada', 'Moderada'), ('Pouca', 'Pouca')], max_length=20, null=True, verbose_name='Intensidade de perda:')),
                ('AFM10', models.CharField(choices=[('Gota', 'Gota'), ('Colher', 'Colher'), ('Jato', 'Jato')], max_length=20, null=True, verbose_name='Quantidade da perda:')),
                ('AFM11', models.CharField(choices=[('Urgência', 'Urgência'), ('Esforço', 'Esforço'), ('Mista', 'Mista'), ('Transbordamento', 'Transbordamento')], max_length=20, null=True, verbose_name='Tipo da incontinência urinária:')),
                ('AFM12', models.DateField(null=True, verbose_name='Início dos sintomas:')),
                ('AFM13', models.IntegerField(verbose_name='Frequência urinária diária:')),
                ('AFM14', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Dor para urinar?')),
                ('AFM15', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Infecção urinária?')),
                ('AFM16', models.IntegerField(null=True, verbose_name='Quantas vezes?')),
                ('AFM17', models.DateField(null=True, verbose_name='Qual a data do último episódio?')),
                ('AFM18', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name=' Uso de forro?')),
                ('AFM19', models.IntegerField(null=True, verbose_name='Quantidade por dia?')),
                ('AFM20', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name=' Enurese?')),
                ('AFM21', models.IntegerField(null=True, verbose_name='Quantidade de vezes?')),
                ('AFM22', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Nocturia?')),
                ('AFM23', models.IntegerField(null=True, verbose_name='Quantidade de vezes?')),
                ('AFM24', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sente protuberância ou algo caindo que pode ver ou sentir na área vaginal?')),
                ('AFM25', models.CharField(choices=[('Unidigital', 'Unidigital'), ('Bidigital', 'Bidigital')], max_length=20, verbose_name='Toque vaginal')),
                ('AFM26', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Desconforto ao toque vaginal?')),
                ('AFM27', models.CharField(choices=[('Ausente', 'Ausente'), ('Suave', 'Suave'), ('Severo', 'Severo')], max_length=20, verbose_name='Dor')),
                ('AFM28', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Sangramento Vaginal')),
                ('AFM29', models.FloatField(verbose_name='Comprimento')),
                ('AFM30', models.IntegerField(verbose_name='Segundos de contração do MAP sustentada')),
                ('AFM31', models.IntegerField(verbose_name='Contrações rápidas sem perder a força')),
                ('AFM32', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Usa musculatura acessória para contração?')),
                ('AFM33', models.CharField(choices=[('Abdômen', 'Abdômen'), ('Glúteos', 'Glúteos'), ('Adutores', 'Adutores')], max_length=20, verbose_name='Musculatura: ')),
                ('AFM34', models.CharField(choices=[('Diminuído', 'Diminuído'), ('Normal', 'Normal'), ('Aumentado', 'Aumentado')], max_length=20, verbose_name='Atividade tônica dos músculos do assoalho pélvico')),
                ('AFM35', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Contração do levantador do ânus/ contração em direção à sínfise púbica')),
                ('AFM36', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Exercícios com dilatadores')),
                ('AFM37', models.IntegerField(null=True, verbose_name='Frequência dilatadores')),
                ('AFM38', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Relação sexual')),
                ('AFM39', models.IntegerField(null=True, verbose_name='Frequência relação sexual')),
                ('AFM40', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, null=True, verbose_name='Desconforto na relação sexual?')),
                ('AFM41', models.CharField(choices=[('0', 'Ausência de resposta muscular'), ('1', 'Esboço de contração não sustentada'), ('2', 'Presença de contração de pequena intensidade, mas que se sustenta'), ('3', 'Contração moderada, sentida com o aumento da pressão intavaginal, que comprime os dedos do examinador com pequena elevação cranial da parede vaginal'), ('4', 'Contração satisfatória, que aperta os dedos do examinador, com elevação da parede vaginal em direção à sínfise púbica'), ('5', 'Contração forte, compressão firme dos dedos do examinador com movimento positivo em relação à sínfise púbica')], max_length=20, verbose_name='Força da musculatura do assoalho pélvico')),
                ('AFM42', models.CharField(choices=[('P', 'Power'), ('E', 'Endurance'), ('R', 'Repetition'), ('F', 'Fast')], max_length=20, verbose_name='Escala New Perfect')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.consulta')),
            ],
        ),
    ]
