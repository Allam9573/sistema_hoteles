from base.models import ClaseModelo
from django.db import models

# Create your models here.


class Empleado(ClaseModelo):
    sueldo = models.DecimalField(max_digits=7, decimal_places=2)
    acceso = models.CharField(max_length=15)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    estado = models.BooleanField(default=True)
