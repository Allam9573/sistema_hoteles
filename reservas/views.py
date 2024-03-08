from django.shortcuts import render
from reservas.models import Reserva
from habitaciones.models import Habitacion
from clientes.models import Cliente


# Create your views here.
def reservas(request):
    reservas = Reserva.objects.all()
    habitaciones = Habitacion.objects.all()
    clientes = Cliente.objects.all()
    return render(
        request,
        "reservas/reservas.html",
        {"reservas": reservas, "habitaciones": habitaciones, "clientes": clientes},
    )


def registrar_reserva(request):
    reservas = Reserva.objects.all()
    habitaciones = Habitacion.objects.all()
    clientes = Cliente.objects.all()
    return render(
        request,
        "reservas/crear.html",
        {"reservas": reservas, "habitaciones": habitaciones, "clientes": clientes},
    )
