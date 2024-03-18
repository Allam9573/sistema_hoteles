from django.db import models
from proveedores.models import Proveedor

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
