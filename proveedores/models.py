from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)