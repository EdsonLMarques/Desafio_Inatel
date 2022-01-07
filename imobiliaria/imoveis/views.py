from django.http import request
from django.shortcuts import redirect, render
from .models import Imovel

def home(request):
    imoveis = Imovel.objects.order_by('codigo')

    dados = {
        'imoveis':imoveis
    }
    return render(request, 'home.html', dados)

def cadastrar(request):
    print("________")
    if request.method == 'POST':
        endereco_imovel = request.POST['end']
        valor_imovel = request.POST['val']
        tipo_imovel = request.POST['t']
        codigo_imovel = request.POST['cod']
        foto_imovel = request.FILES['img']
        imovel = Imovel.objects.create(
            codigo = codigo_imovel,
            tipo = tipo_imovel,
            endereco = endereco_imovel,
            valor = valor_imovel,
            foto_imovel  = foto_imovel,
        )
        print(imovel.codigo)
        imovel.save()
        return redirect('cadastrar_imovel')
    else:
        return render(request, 'cadastrar_imovel.html')