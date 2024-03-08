from django.db import models


# Create your models here.
class Habitacion(models.Model):
    numero_habitacion = models.IntegerField()
    piso = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=100)
    caracteristicas = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=15)
    tipo_habitacion = models.CharField(max_length=20)
