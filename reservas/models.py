from django.db import models
from clientes.models import Cliente
from habitaciones.models import Habitacion
from servicios.models import Servicio
# Create your models here.


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    costo_subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    dias_hospedados = models.IntegerField(default=0)
    consumos = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    total_consumos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
