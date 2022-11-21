from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hotel
from .models import Sucursal
from .models import Turista
from .models import Vuelo
from .forms import HotelForm
from .forms import SucursalForm
from .forms import TuristaForm
from .forms import VueloForm
# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def hotel(request):
    hoteles = Hotel.objects.all()
    return render(request, 'hotel/index.html', {'hoteles': hoteles})
def hotelCrear(request):
    form = HotelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('hotel')
    return render(request, 'hotel/crear.html', {'form': form})
def hotelEditar(request, idhotel):
    hotel = Hotel.objects.get(idhotel=idhotel)
    form = HotelForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('hotel')
    return render(request, 'hotel/editar.html', {'form': form})
def hotelEliminar(request, idhotel):
    hotel = Hotel.objects.get(idhotel=idhotel)
    hotel.delete()
    return redirect('hotel')

def sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/index.html', {'sucursales': sucursales})
def sucursalCrear(request):
    form = SucursalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sucursal')
    return render(request, 'sucursal/crear.html', {'form': form})
def sucursalEditar(request, idsucursal):
    sucursal = Sucursal.objects.get(idsucursal=idsucursal)
    form = SucursalForm(request.POST or None, instance=sucursal)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('sucursal')
    return render(request, 'sucursal/editar.html', {'form': form})
def sucursalEliminar(request, idsucursal):
    sucursal = Sucursal.objects.get(idsucursal=idsucursal)
    sucursal.delete()
    return redirect('sucursal')

def turista(request):
    turistas = Turista.objects.all()
    return render(request, 'turista/index.html', {'turistas': turistas})
def turistaCrear(request):
    form = TuristaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('turista')
    return render(request, 'turista/crear.html', {'form': form})
def turistaEditar(request, idturista):
    turista = Turista.objects.get(idturista=idturista)
    form = TuristaForm(request.POST or None, instance=turista)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('turista')
    return render(request, 'turista/editar.html', {'form': form})
def turistaEliminar(request, idturista):
    turista = Turista.objects.get(idturista=idturista)
    turista.delete()
    return redirect('turista')

def vuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request, 'vuelo/index.html', {'vuelos': vuelos})
def vueloCrear(request):
    form = VueloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vuelo')
    return render(request, 'vuelo/crear.html', {'form' : form})
def vueloEditar(request, idvuelo):
    vuelo = Vuelo.objects.get(idvuelo=idvuelo)
    form = VueloForm(request.POST or None, instance=vuelo)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('vuelo')
    return render(request, 'vuelo/editar.html', {'form': form})
def vueloEliminar(request, idvuelo):
    vuelo = Vuelo.objects.get(idvuelo=idvuelo)
    vuelo.delete()
    return redirect('vuelo')