# Generated by Django 4.1.7 on 2023-03-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituicao', '0002_remove_instituicao_id_administrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='senha',
            field=models.CharField(max_length=128),
        ),
    ]