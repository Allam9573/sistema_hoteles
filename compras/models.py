from django.db import models
from proveedores.models import Proveedor

# Create your models here.
class Compra(models.Model):
    tipo_compra = models.CharField(max_length=15)
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
