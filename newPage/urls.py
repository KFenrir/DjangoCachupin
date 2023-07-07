from django.urls import path

from .views import  agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from . import views

urlpatterns = [
    path("main", views.main, name="main"), 
    path("login",views.login, name="login"),
    path("gatos", views.gatos, name="gatos"),
    path("perros", views.perros, name="perros"),
    path("arnes_gatos", views.arnes_gatos, name="arnes_gatos"),
    path("bandana_gatos", views.bandana_gatos, name="bandana_gatos"),
    path("collar_gatos", views.collar_gatos, name="collar_gatos"),
    path("arnes_perros", views.arnes_perros, name="arnes_perros"),
    path("bandana_perros", views.bandana_perros, name="bandana_perros"),
    path("collar_perros", views.collar_perros, name="collar_perros"),
    path("carrito", views.Carrito, name="carrito"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("registro", views.registro, name="registro"),
    path("tallas", views.tallas, name="tallas"),
    path("suscripciones", views.suscripciones, name="suscripciones"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("tienda", views.tienda, name="Tienda"),
    path('agregar/<int:producto_id>/',agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/',eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/',restar_producto, name="Sub"),
]