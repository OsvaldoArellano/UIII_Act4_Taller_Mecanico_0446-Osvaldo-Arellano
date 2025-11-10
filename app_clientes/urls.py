from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_taller, name='inicio_taller'),
    path('clientes/agregar/', views.agregar_clientes, name='agregar_clientes'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/editar/<int:cliente_id>/', views.actualizar_clientes, name='actualizar_clientes'),
    path('clientes/editar/guardar/<int:cliente_id>/', views.realizar_actualizacion_clientes, name='realizar_actualizacion_clientes'),
    path('clientes/borrar/<int:cliente_id>/', views.borrar_clientes, name='borrar_clientes'),
    
    path('servicios/', views.ver_servicio, name='ver_servicio'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/actualizar/<int:servicio_id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/actualizar/confirmar/<int:servicio_id>/', views.realizar_actualizacion_servicio, name='realizar_actualizacion_servicio'),
    path('servicios/borrar/<int:servicio_id>/', views.borrar_servicio, name='borrar_servicio'),
]