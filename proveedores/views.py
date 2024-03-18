from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.


def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/proveedores.html", {"proveedores": proveedores})


def guardar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        contacto = request.POST['contacto']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        nuevo_proveedor = Proveedor(
            nombre=nombre,
            contacto=contacto,
            correo=correo,
            telefono=telefono
        )
        nuevo_proveedor.save()
        return redirect("proveedores")
    else:
        return redirect("proveedores")
