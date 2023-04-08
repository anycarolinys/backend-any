from django.db import models
from instituicao.models import Instituicao

class Fisioterapeuta(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    instituicao = models.ForeignKey(Instituicao, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome