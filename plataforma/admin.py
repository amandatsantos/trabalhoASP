from django.contrib import admin
from .models import Carro, Reserva, Cliente
from .forms import ReservaForm, CarroForm, CustomUserCreationForm

class CarroAdmin(admin.ModelAdmin):
    form = CarroForm
    list_display = ('marca', 'modelo', 'ano', 'preco_diaria', 'disponivel')
    search_fields = ('marca', 'modelo')
    list_filter = ('disponivel', 'marca', 'modelo')

class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm
    list_display = ('usuario', 'carro', 'data_reserva', 'data_inicio', 'data_fim')
    search_fields = ('usuario__username', 'carro__modelo')
    list_filter = ('data_reserva', 'data_inicio', 'data_fim')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'endereco', 'email', 'idade')
    search_fields = ('user__username', 'email')
    list_filter = ('idade',)

admin.site.register(Carro, CarroAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Cliente, ClienteAdmin)
