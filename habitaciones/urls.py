from django.urls import path
from . import views

urlpatterns = [
    path("", views.habitaciones, name="habitaciones"),
    path("nueva-habitacion/", views.registrar_habitacion, name="registrar_habitacion"),
    path('api/guardar-habitacion/', views.guardar_habitacion, name='guardar_habitacion')
]
