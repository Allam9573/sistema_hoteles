from django.urls import path
from . import views

urlpatterns = [
    path("", views.proveedores, name="proveedores"),
    path("api/guardar-proveedor", views.guardar_proveedor, name="guardar_proveedor")
]
