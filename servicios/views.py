from django.shortcuts import render, HttpResponse
from .models import Servicio


# Create your views here.
def crear_servicio(request):
    nuevo_servicio = Servicio(nombre="Pescado Frito con Tajadas", precio=90)
    nuevo_servicio.save()
    return HttpResponse("Servicio creado")
