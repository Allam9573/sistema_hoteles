from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservas, name="reservas"),
    path("nueva-reserva/", views.registrar_reserva, name="registrar_reserva"),
    path('api/guardar-reserva/', views.guardar_reserva, name='guardar_reserva'),
    path('view/<int:id>/', views.ver_reserva)
]
