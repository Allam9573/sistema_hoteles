from django.shortcuts import render, redirect
from facturas.models import Factura
from reservas.models import Reserva
from flujo_caja.models import Flujo_Caja


# Create your views here.
def facturas(request):
    facturas = Factura.objects.all()
    flujo_caja = Flujo_Caja.objects.get(id=1)
    return render(
        request,
        "facturas/facturas.html",
        {"facturas": facturas, "flujo_caja": flujo_caja},
    )


def crear_factura(request):
    if request.method == "POST":
        flujo_caja = Flujo_Caja.objects.get(id=1)
        reserva = Reserva.objects.get(id=int(request.POST["reserva_id"]))
        monto = float(request.POST["monto"])
        cambio = 0
        if monto > reserva.costo_subtotal:
            cambio = monto - float(reserva.costo_subtotal)

        flujo_caja.ingresos_totales += reserva.costo_subtotal
        nueva_factura = Factura(reserva=reserva, cambio=cambio, monto_ingresado=monto)
        nueva_factura.save()
        flujo_caja.save()
        return redirect("facturas")
    else:
        return redirect("facturas")
