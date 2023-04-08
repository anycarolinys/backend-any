from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=45)

    def __str__(self):
        return self.nome
    
