from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)