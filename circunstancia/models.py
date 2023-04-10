from django.db import models

CIRCUNSTANCIA = [('Tosse','Tosse'), ('Espirro','Espirro'), ('Andar','Andar'), ('Riso','Riso'), ('Pular','Pular'),
                ('Pegar peso','Pegar peso'), ('Relação sexual','Relação sexual')]

class Circunstancia(models.Model):
    circunstancia = models.CharField(max_length=20, choices=CIRCUNSTANCIA)

    def __str__(self):
        return str(self.circunstancia)
