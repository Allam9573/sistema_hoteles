from django.urls import path
from . import views

urlpatterns = [
    path("", views.facturas, name="facturas"),
    path("nueva-factura/", views.crear_factura, name="crear_factura"),
]
