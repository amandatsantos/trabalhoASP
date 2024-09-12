from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial com os carros disponíveis
    path('login/', views.login_view, name='login'),  # Página de login
    path('cadastro/', views.cadastro_view, name='cadastro'),  # Página de cadastro
    path('minhas_reservas/', views.minhas_reservas, name='reservas_confirmadas'),  # Página de reservas do usuário
    path('reservar_carro/<int:carro_id>/', views.reservar_carro, name='reservar_carro'),# Página de reserva de carro
    path('reservas_confirmadas/', views.reservas_confirmadas, name='reservas_confirmadas')
]