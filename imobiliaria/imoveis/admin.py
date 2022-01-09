from django.contrib import admin
from .models import Imovel, Alugueis

modelos = [Imovel, Alugueis]

admin.site.register(modelos)