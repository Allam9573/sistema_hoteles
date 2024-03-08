from django.shortcuts import render, redirect
from clientes.models import Cliente


# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/clientes.html", {"clientes": clientes})


def registrar_cliente(request):
    return render(request, "clientes/crear.html")


def guardar_cliente(request):
    if request.method == "POST":
        nombre_completo = request.POST["nombre_completo"]
        correo = request.POST["correo"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        tipo_documento = request.POST["tipo_documento"]
        numero_documento = request.POST["numero_documento"]
        nuevo_cliente = Cliente(
            nombre=nombre_completo,
            correo=correo,
            direccion=direccion,
            telefono=telefono,
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
        )
        nuevo_cliente.save()
        return redirect("clientes")
    else:
        return redirect("clientes")


def ver_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "clientes/editar.html")


def ver_eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "clientes/eliminar.html", {"cliente": cliente})


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("clientes")
