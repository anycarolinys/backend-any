# Generated by Django 4.1.7 on 2023-03-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisioterapeuta', '0003_remove_fisioterapeuta_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisioterapeuta',
            name='senha',
            field=models.CharField(max_length=128),
        ),
    ]
