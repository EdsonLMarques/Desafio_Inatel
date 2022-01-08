from django.db import models
from datetime import datetime
from cliente.models import Cliente

class Imovel(models.Model):
    codigo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    foto_imovel = models.ImageField(upload_to = 'fotos/%d/%m/%Y', blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo

# Registro de locação, relacionando o imóvel a um cliente em um período (início, término)
class Alugueis(models.Model):
    imóvel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicial = models.DateTimeField(default=datetime.now, blank=True)
    data_final = models.DateTimeField(default=datetime.now, blank=True)