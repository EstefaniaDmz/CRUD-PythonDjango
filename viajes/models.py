from django.db import models

# Create your models here.

class Turista(models.Model):
    idturista = models.AutoField(primary_key=True, verbose_name='idTurista')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellidoM = models.CharField(max_length=50, verbose_name='Apellido Materno')
    apellidoP = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    codigopostal = models.CharField(max_length=5, verbose_name='Código Postal')
    calle = models.CharField(max_length=100, verbose_name='Calle')
    colonia = models.CharField(max_length=100, verbose_name='Colonia')
    idhotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, verbose_name='idHotel')
    regimen = models.CharField(max_length=50, verbose_name='Regimen')
    idsucursal = models.ForeignKey("Sucursal", on_delete=models.CASCADE, verbose_name='idSucursal')
    idvuelo = models.ForeignKey("Vuelo", on_delete=models.CASCADE, verbose_name='idVuelo')
    claseTurista = models.CharField(max_length=50, verbose_name='Clase del Vuelo')
    estatus = models.BooleanField(default=True, verbose_name='Estatus')

    def __str__(self):
        fila = self.apellidoP + " " + self.apellidoM + " " + self.nombre + " - " + self.telefono
        return fila

class Hotel(models.Model):
    idhotel = models.AutoField(primary_key=True, verbose_name='idHotel')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    numeroplazas = models.IntegerField(verbose_name='Número de plazas')
    codigopostal = models.CharField(max_length=5, verbose_name='Código postal')
    calle = models.CharField(max_length=100, verbose_name='Calle')
    colonia = models.CharField(max_length=100, verbose_name='Colonia')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    estado = models.CharField(max_length=100, verbose_name='Estado')
    pais = models.CharField(max_length=100, verbose_name='País')
    estatus = models.BooleanField(default=True, verbose_name='Estatus')

    def __str__(self):
        fila = self.nombre + " - " + self.telefono
        return fila

class Sucursal(models.Model):
    idsucursal = models.AutoField(primary_key=True, verbose_name='idSucursal')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')
    numeroplazas = models.IntegerField(verbose_name='Número de plazas')
    codigopostal = models.CharField(max_length=5, verbose_name='Código postal')
    calle = models.CharField(max_length=100, verbose_name='Calle')
    colonia = models.CharField(max_length=100, verbose_name='Colonia')
    estatus = models.BooleanField(default=True, verbose_name='Estatus')

    def __str__(self):
        fila = self.nombre + " - " + self.telefono
        return fila

class Vuelo(models.Model):
    idvuelo = models.AutoField(primary_key=True, verbose_name='idVuelo')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')
    numeroplazas = models.IntegerField(verbose_name='Número de plazas')
    ciudadOrigen = models.CharField(max_length=100, verbose_name='Ciudad de Origen')
    estadoOrigen = models.CharField(max_length=100, verbose_name='Estado de Origen')
    paisOrigen = models.CharField(max_length=100, verbose_name='País de Origen')
    ciudadDestino = models.CharField(max_length=100, verbose_name='Ciudad de Destino')
    estadoDestino = models.CharField(max_length=100, verbose_name='Estado de Destino')
    paisDestino = models.CharField(max_length=100, verbose_name='País de Destino')
    estatus = models.BooleanField(default=True, verbose_name='Estatus')

    def __str__(self):
        fila = "De " + self.estadoOrigen + ", " + self.paisOrigen + " a " + self.estadoDestino + ", " + self.paisDestino
        return fila
