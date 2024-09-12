from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages

from plataforma.forms import CustomUserCreationForm
from .models import Carro, Reserva

# View para exibir os carros disponíveis na home
def home(request):
    carros = Carro.objects.filter(disponivel=True)
    return render(request, 'home.html', {'carros': carros})

# View para realizar login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Erro ao processar o formulário.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# View para cadastro de novo cliente
def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

# View para exibir as reservas do cliente logado
@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas_confirmadas.html', {'reservas': reservas})

@login_required
def reservas_confirmadas(request):
    # Obtém todas as reservas feitas pelo usuário logado
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas_confirmadas.html', {'reservas': reservas})

@login_required
def reservar_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)

    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')

        # Cria a reserva
        Reserva.objects.create(
            usuario=request.user,
            carro=carro,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        # Atualiza a disponibilidade do carro
        carro.disponivel = False
        carro.save()

        return redirect('reservas_confirmadas')  # Redireciona para a página de confirmação

    return render(request, 'home.html', {'carros_disponiveis': Carro.objects.filter(disponivel=True)})

