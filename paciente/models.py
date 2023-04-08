from django.db import models 

class Paciente(models.Model):
    matricula = models.CharField(max_length=45, unique=True)
    nome = models.CharField(max_length=100)
    altura = models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField()
    cpf = models.CharField(max_length=15, unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()    

    def __str__(self) -> str:
        return self.nome
