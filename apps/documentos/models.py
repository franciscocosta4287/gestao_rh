from django.db import models

# Create your models here.
from apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=255)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao