from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome_depart = models.CharField(max_length=100, help_text="Nome do Departamento")

    def __str__(self):
        return self.nome_depart