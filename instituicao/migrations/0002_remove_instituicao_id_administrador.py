# Generated by Django 4.1.7 on 2023-03-09 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='id_administrador',
        ),
    ]
