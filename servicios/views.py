from django.shortcuts import render, HttpResponse
from .models import Servicio


# Create your views here.
def crear_servicio(request):
    nuevo_servicio = Servicio("Almuerzo Costeño", 90)
    nuevo_servicio.save()
    return HttpResponse("Servicio creado")
