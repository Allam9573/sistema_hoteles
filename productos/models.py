from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=20)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2)
