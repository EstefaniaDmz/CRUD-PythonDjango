from django import forms
from .models import Hotel
from .models import Turista
from .models import Sucursal
from .models import Vuelo

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre', 'telefono', 'numeroplazas', 'codigopostal', 'calle', 'colonia', 'ciudad', 'estado', 'pais']

class TuristaForm(forms.ModelForm):
    class Meta:
        model = Turista
        fields = ['nombre', 'apellidoP', 'apellidoM', 'telefono', 'codigopostal', 'calle', 'colonia', 'idhotel', 'regimen', 'idsucursal', 'idvuelo', 'claseTurista']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'telefono', 'numeroplazas', 'codigopostal', 'calle', 'colonia']

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['fecha', 'hora', 'numeroplazas', 'ciudadOrigen', 'estadoOrigen', 'paisOrigen', 'ciudadDestino', 'estadoDestino', 'paisDestino']