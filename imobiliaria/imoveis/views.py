from django.http import request, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import Imovel, Alugueis
from cliente.models import Cliente
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        vaga = request.POST['vago']
        if tipo == 'tipo1': #sem filtro
            if vaga == 'vago1':
                imoveis = Imovel.objects.order_by('codigo')
            elif vaga == 'vago2':
                imoveis = Imovel.objects.order_by('codigo').filter(status=False)
            else:
                imoveis = Imovel.objects.order_by('codigo').filter(status=True)
        if tipo == 'tipo2': #sem filtro
            if vaga == 'vago1':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='2')
            elif vaga == 'vago2':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='2', status=False)
            else:
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='2', status=True)
        if tipo == 'tipo3': #sem filtro
            if vaga == 'vago1':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='3')
            elif vaga == 'vago2':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='3', status=False)
            else:
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='3', status=True)
        if tipo == 'tipo4': #sem filtro
            if vaga == 'vago1':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='1')
            elif vaga == 'vago2':
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='1', status=False)
            else:
                imoveis = Imovel.objects.order_by('codigo').filter(tipo='1', status=True)

        dados = {
            'imoveis':imoveis
        }

        return render(request, 'home.html', dados)
    else:
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
            imovel_compromissado.status = True
            imovel_compromissado.save()
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
