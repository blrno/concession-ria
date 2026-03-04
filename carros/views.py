from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import RegistrarForm, CarroForm
from .models import Carro
from django.db.models import Sum

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('lista_carros')
    else:
        form = AuthenticationForm()
    return render(request, 'carros/login.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça seu login.')
            return redirect('login')
    else:
        form = RegistrarForm()
    
    return render(request, 'carros/registrar.html', {'form': form})

def lista_carros(request):
    carros = Carro.objects.all()
    total_veiculos = carros.count()
    valor_total = carros.aggregate(Sum('preco'))['preco__sum'] or 0
    return render(request, 'carros/lista_carros.html', {
        'carros': carros,
        'total_veiculos': total_veiculos,
        'valor_total': valor_total
    })

# 4. CADASTRAR NOVO CARRO
def cadastrar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carros')
    else:
        form = CarroForm()
    return render(request, 'carros/form_carro.html', {'form': form})

# 5. EXCLUIR CARRO
def excluir_carro(request, id):
    carro = get_object_or_404(Carro, id=id)
    carro.delete()
    return redirect('lista_carros')

# 6. LOGOUT
def logout_view(request):
    auth_logout(request)
    return redirect('login')