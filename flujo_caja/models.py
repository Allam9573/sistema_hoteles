from django.db import models


# Create your models here.
class Flujo_Caja(models.Model):
    ingresos_totales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
