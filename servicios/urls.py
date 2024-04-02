from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_servicio, name='crear_servicio')
]
