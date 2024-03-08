from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservas, name="reservas"),
    path("nueva-reserva/", views.registrar_reserva, name="registrar_reserva"),
]
