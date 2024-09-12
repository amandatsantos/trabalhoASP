
from django.db import models
from django.contrib.auth.models import User

class Carro(models.Model):
    MODELO_CHOICES = [
        ('SUV', 'SUV'),
        ('Pickup', 'Pickup'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
    ]

    MARCA_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
    ]

    modelo = models.CharField(max_length=50, choices=MODELO_CHOICES)
    marca = models.CharField(max_length=50, choices=MARCA_CHOICES)
    ano = models.PositiveIntegerField()
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='carros/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.carro.modelo}"


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nome =  models.CharField(max_length=15)
    idade =  models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    email = models.EmailField()  # Define o email como único e obrigatório

    def __str__(self):
        return self.user.username