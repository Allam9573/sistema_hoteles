from django.db import models
from reservas.models import Reserva

# Create your models here.


class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cambio = models.DecimalField(max_digits=10, decimal_places=2)
    monto_ingresado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
