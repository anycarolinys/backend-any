# Generated by Django 4.1.7 on 2023-04-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circunstancia',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('circunstancia', models.CharField(choices=[('Tosse', 'Tosse'), ('Espirro', 'Espirro'), ('Andar', 'Andar'), ('Riso', 'Riso'), ('Pular', 'Pular'), ('Pegar peso', 'Pegar peso'), ('Relação sexual', 'Relação sexual')], max_length=20)),
            ],
        ),
    ]
