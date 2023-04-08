# Generated by Django 4.1.7 on 2023-03-05 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=45)),
                ('id_administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracao.administrador')),
            ],
        ),
    ]
