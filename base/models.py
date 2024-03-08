from django.db import models


# Create your models here.
class ClaseModelo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)

    class Meta:
        abstract = True
