from django.http import request
from django.shortcuts import render
from .models import Imovel

def home(request):
    imoveis = Imovel.objects.order_by('codigo')

    dados = {
        'imoveis':imoveis
    }
    return render(request, 'home.html', dados)

def imovel(request):
    return render(request, 'imovel.html')