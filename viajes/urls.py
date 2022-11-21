from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel', views.hotel, name='hotel'),
    path('hotelCrear', views.hotelCrear, name='hotelCrear'),
    path('hotelEditar/<int:idhotel>', views.hotelEditar, name='hotelEditar'),
    path('hotelEliminar/<int:idhotel>', views.hotelEliminar, name='hotelEliminar'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('sucursalCrear', views.sucursalCrear, name='sucursalCrear'),
    path('sucursalEditar/<int:idsucursal>', views.sucursalEditar, name='sucursalEditar'),
    path('sucursalEliminar/<int:idsucursal>', views.sucursalEliminar, name='sucursalEliminar'),
    path('turista', views.turista, name='turista'),
    path('turistaCrear', views.turistaCrear, name='turistaCrear'),
    path('turistaEditar/<int:idturista>', views.turistaEditar, name='turistaEditar'),
    path('turistaEliminar/<int:idturista>', views.turistaEliminar, name='turistaEliminar'),
    path('vuelo', views.vuelo, name='vuelo'),
    path('vueloCrear', views.vueloCrear, name='vueloCrear'),
    path('vueloEditar/<int:idvuelo>', views.vueloEditar, name='vueloEditar'),
    path('vueloEliminar/<int:idvuelo>', views.vueloEliminar, name='vueloEliminar'),
]