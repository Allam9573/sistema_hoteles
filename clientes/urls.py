from django.urls import path
from . import views

urlpatterns = [
    path("", views.clientes, name="clientes"),
    path("nuevo/", views.registrar_cliente, name="registrar_cliente"),
    path("api/guardar-cliente/", views.guardar_cliente, name="guardar_cliente"),
    path("ver/<int:id>/", views.ver_cliente),
    path("eliminar/<int:id>/", views.ver_eliminar),
    path("api/eliminar/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),
]
