from django.shortcuts import render, redirect
from reservas.models import Reserva
from habitaciones.models import Habitacion
from clientes.models import Cliente
from datetime import datetime
from servicios.models import Servicio


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


def guardar_reserva(request):
    if request.method == "POST":
        cliente = Cliente.objects.get(id=int(request.POST["cliente"]))
        habitacion = Habitacion.objects.get(id=int(request.POST["habitacion"]))
        fecha_ingreso_str = request.POST.get("fecha_ingreso")
        fecha_salida_str = request.POST.get("fecha_salida")
        fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
        fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d")
        diferencia = fecha_salida - fecha_ingreso
        dias = diferencia.days
        subtotal = habitacion.precio * dias
        nueva_reserva = Reserva(
            cliente=cliente,
            habitacion=habitacion,
            fecha_ingreso=fecha_ingreso_str,
            fecha_salida=fecha_salida_str,
            costo_subtotal=subtotal,
            dias_hospedados=dias,
        )
        nueva_reserva.save()
        return redirect("reservas")
    else:
        return redirect("reservas")


def ver_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    servicios = Servicio.objects.all()
    return render(request, "reservas/ver.html", {"reserva": reserva, "servicios": servicios})


def ver_reserva_eliminar(request, id):
    reserva = Reserva.objects.get(id=id)
    return render(request, "reservas/eliminar.html", {"reserva": reserva})


def eliminar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect("reservas")


def agregar_consumo(request):
    reserva = Reserva.objects.get(id=int(request.POST['id_reserva']))
    servicio = Servicio.objects.get(id=int(request.POST['id_servicio']))
    reserva.consumos = servicio
    reserva.save()
    return redirect('reservas')
