from django.urls import path
from . import views

urlpatterns = [
    path("", views.productos, name="productos"),
    path("api/guardar-producto/", views.guardar_producto, name="guardar_producto"),
]
