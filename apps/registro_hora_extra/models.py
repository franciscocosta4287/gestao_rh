from django.db import models

# Create your models here.
from apps.funcionarios.models import Funcionario

# Create your models here.
class RegistroHE(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo