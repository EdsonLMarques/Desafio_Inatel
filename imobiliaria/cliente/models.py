from django.db import models
# nome, email e telefone do cliente.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    def __str__(self):
        return self.nome
    