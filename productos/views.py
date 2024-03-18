from django.shortcuts import render, redirect
from productos.models import Producto
from proveedores.models import Proveedor


# Create your views here.
def productos(request):
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    return render(
        request,
        "productos/productos.html",
        {"proveedores": proveedores, "productos": productos},
    )


def guardar_producto(request):
    nombre = request.POST["nombre"]
    cantidad = int(request.POST["cantidad"])
    proveedor = Proveedor.objects.get(id=int(request.POST["proveedor"]))
    precio = float(request.POST["precio"])
    buscar_producto = Producto.objects.filter(nombre=nombre)
    if buscar_producto:
        buscar_producto[0].existencia += cantidad
        buscar_producto[0].save()
        return redirect("productos")
    else:
        nuevo_producto = Producto(
            nombre=nombre, proveedor=proveedor, precio=precio, existencia=cantidad
        )
        nuevo_producto.save()
        return redirect("productos")
