from django.urls import path
from . import views

urlpatterns = [
    path("", views.reservas, name="reservas"),
    path("nueva-reserva/", views.registrar_reserva, name="registrar_reserva"),
    path('api/guardar-reserva/', views.guardar_reserva, name='guardar_reserva'),
    path('view/<int:id>/', views.ver_reserva, name='ver_reserva'),
    path('eliminar/<int:id>/', views.ver_reserva_eliminar, name='ver_reserva_eliminar'),
    path('api/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('api/agregar-consumo/', views.agregar_consumo, name='agregar_consumo')
]
