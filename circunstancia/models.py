from django.db import models
from formularios.formAFM.models import FormAFM

# Create your models here.
class Circunstancia(models.Model):
    # id = models.AutoField(primary_key=True)
    circunstancia = models.CharField(max_length=20)
    formAFM  = models.ForeignKey(FormAFM, on_delete=models.DO_NOTHING, related_name='AFM06')

    def __str__(self):
        return str(self.circunstancia)
