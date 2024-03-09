from django.shortcuts import render, redirect
from clientes.models import Cliente
from habitaciones.models import Habitacion
from reservas.models import Reserva


def index(request):
    return redirect("home/")


def home(request):
    clientes = Cliente.objects.count()
    habitaciones = Habitacion.objects.count()
    reservas = Reserva.objects.count()
    return render(request, "home.html", {'clientes': clientes, 'habitaciones': habitaciones, 'reservas': reservas})
