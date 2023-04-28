from django.db import models

class Modelo(models.Model):
    Descricao = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome

class Marca(models.Model):
    Marca = models.CharField(max_length=50)
    Nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.Marca

class Cor(models.Model):
    Cores = models.CharField(max_length=100)

    def __str__(self):
        return self.Cores


     


class veiculo(models.Model):
        Marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Marcas")
        Modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="Modelo")
        Cor = models.ForeignKey(Cor,on_delete=models.PROTECT, related_name="Coress")
        Ano = models.IntegerField(default=0, null=True, blank=True)
        Preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True )
        
        def __str__(self): 
             return f"{self.Marca}, {self.Modelo}, {self.Ano}, {self.Cor}"