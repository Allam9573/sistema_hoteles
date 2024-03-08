from django.shortcuts import render, redirect
from habitaciones.models import Habitacion


# Create your views here.
def habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(
        request, "habitaciones/habitaciones.html", {"habitaciones": habitaciones}
    )


def registrar_habitacion(request):
    return render(request, "habitaciones/crear.html")


def guardar_habitacion(request):
    if request.method == "POST":
        numero_habitacion = request.POST["numero_habitacion"]
        piso = request.POST["piso"]
        descripcion = request.POST["descripcion"]
        caracteristicas = request.POST["caracteristicas"]
        precio = request.POST["precio"]
        estado = request.POST["estado"]
        tipo_habitacion = request.POST["tipo_habitacion"]
        nueva_habitacion = Habitacion(
            numero_habitacion=numero_habitacion,
            piso=piso,
            descripcion=descripcion,
            caracteristicas=caracteristicas,
            precio=precio,
            estado=estado,
            tipo_habitacion=tipo_habitacion,
        )
        nueva_habitacion.save()
        return redirect("habitaciones")
    else:
        return redirect("habitaciones")
