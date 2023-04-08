from django.db import models
from instituicao.models import Instituicao

class Administrador(models.Model):
    login = models.CharField(max_length=45, unique=True)
    senha = models.CharField(max_length=128)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.login
