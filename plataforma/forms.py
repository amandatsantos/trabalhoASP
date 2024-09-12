from django import forms
from django.contrib import admin
from .models import Reserva, Carro, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['carro', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'preco_diaria', 'disponivel', 'imagem']

# forms.py


class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=15, required=True)
    idade = forms.CharField(max_length=15, required=True)
    telefone = forms.CharField(max_length=15, required=True)
    endereco = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)  # Adicione required=True se ainda não estiver lá

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nome','email', 'telefone', 'endereco', 'idade']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Verifica se já existe um Cliente para o usuário
            cliente, created = Cliente.objects.get_or_create(
                user=user,
                defaults={
                    'nome': self.cleaned_data['nome'],
                    'idade': self.cleaned_data['idade'],
                    'telefone': self.cleaned_data['telefone'],
                    'endereco': self.cleaned_data['endereco'],
                    'email': self.cleaned_data['email']
                }
            )
            # Se o cliente já existia, atualiza os campos
            if not created:
                cliente.nome =  self.cleaned_data['nome']
                cliente.idade = self.cleaned_data['idade']
                cliente.telefone = self.cleaned_data['telefone']
                cliente.endereco = self.cleaned_data['endereco']
                cliente.email = self.cleaned_data['email']
                cliente.save()
        return user