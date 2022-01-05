from django.db import models


class Imovel(models.Model):
    codigo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    foto_imovel    = models.ImageField(upload_to = 'fotos/%d/%m/%Y', blank=True)
    def __str__(self):
        return self.codigo