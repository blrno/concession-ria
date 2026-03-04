from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'