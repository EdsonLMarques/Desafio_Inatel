from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Imovel, Alugueis
from cliente.models import Cliente
from django.contrib import messages

def home(request):
    imoveis = Imovel.objects.order_by('codigo')
    dados = {
        'imoveis':imoveis
    }
    return render(request, 'home.html', dados)

def cadastrar(request):
    if request.method == 'POST':
        endereco_imovel = request.POST['end']
        valor_imovel = request.POST['val']
        tipo_imovel = request.POST['t']
        codigo_imovel = request.POST['cod']
        foto_imovel = request.FILES['imagem']
        imovel = Imovel.objects.create(
            codigo = codigo_imovel,
            tipo = tipo_imovel,
            endereco = endereco_imovel,
            valor = valor_imovel,
            foto_imovel  = foto_imovel,
        )
        print(imovel.codigo)
        imovel.save()
        return redirect('cadastrar')
    else:
        return render(request, 'cadastrar_imovel.html')

def imovel(request, imovel_id):
    if request.method == 'POST':
        imovel_compromissado = get_object_or_404(Imovel, pk=imovel_id)
        print(imovel_compromissado)
        aux_cliente = request.POST['cliente']
        cliente_compromissado = get_object_or_404(Cliente, pk=aux_cliente)
        d_inicial = request.POST['inicial']
        d_final = request.POST['final']
        if d_inicial < d_final:
            aluguel = Alugueis.objects.create(
                imóvel = imovel_compromissado,
                cliente = cliente_compromissado,
                data_inicial = d_inicial,
                data_final = d_final,
            )
            aluguel.save()
            return redirect('home')
        else: 
            messages.info(request, 'Data inicial maior que final')
            return HttpResponseRedirect(request.path_info)
    else:
        imovel = get_object_or_404(Imovel, pk=imovel_id)
        clientes = Cliente.objects.order_by('pk')
        imovel_a_exibir = {
            'imovel' : imovel,
            'clientes' : clientes
        }
        return render(request, 'imovel.html', imovel_a_exibir)