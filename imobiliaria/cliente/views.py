from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Cliente

# nome, email e telefone do cliente.
# Create your views here.
def cliente(request):
    if request.method == 'POST':
        nome_cliente = request.POST['nome']
        email_cliente = request.POST['email']
        telefone_cliente = request.POST['telefone']
        cliente = Cliente.objects.create(
            nome = nome_cliente,
            email = email_cliente,
            telefone = telefone_cliente,
        )
        print(cliente.nome)
        cliente.save()
        return redirect('cliente')
    else:
        return render(request, 'cliente.html')  
