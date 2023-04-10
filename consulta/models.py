from django.db import models
from paciente.models import Paciente
from fisioterapeuta.models import Fisioterapeuta

class Consulta(models.Model):
    data_consulta = models.DateField(auto_now_add=True)
    data_retorno = models.DateField(null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente')
    fisioterapeuta = models.ForeignKey(Fisioterapeuta, on_delete=models.CASCADE, related_name='fisioterapeuta')

    def __str__(self):
        return str(self.paciente)
