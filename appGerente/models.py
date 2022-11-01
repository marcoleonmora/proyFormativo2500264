from datetime import date
from tabnanny import verbose
from django.db import models
from appAdmin.models import *

# --------------------------------------------------------------------------
class Finca(models.Model):
    nombreFinca = models.CharField(max_length=100, null=False)
    nombreGerente = models.CharField(max_length=100, null=False)
    apellidoGerente = models.CharField(max_length=100, null=False, default='')
    nitFinca = models.IntegerField(null=False)
    correoGerente = models.CharField(max_length=100, null=False)
    cedulaGerente = models.CharField(max_length=20, null=False)
    ubicacionFinca = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nombreFinca

# --------------------------------------------------------------------------
class Lote(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    observacLote = models.CharField(max_length=300, null=True)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=False)
    descripLote = models.CharField(max_length=100, null=False)
    areaLote = models.IntegerField(null=False)

    def __str__(self):
        return  "{} - {}".format(self.finca, self.descripLote ) 

# --------------------------------------------------------------------------
class Indirecto(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    fechaPago = models.DateField(default= date.today)
    numFactura = models.CharField(max_length=20, null=False)
    observacPago = models.CharField(max_length=200, null=False)
    valorPagado = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.observacPago

# --------------------------------------------------------------------------
class EquipoFinca(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=False)
    existenciaEquipo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valorUnitarioEquipo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    deprecEquipo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.equipo

# --------------------------------------------------------------------------
class CompraEquipo(models.Model):
    equipoFinca = models.ForeignKey(EquipoFinca, on_delete=models.CASCADE, null=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
    fechaCompraEquipo = models.DateField(default= date.today)
    numFactura = models.CharField(max_length=20, null=False)
    cantidadCompraEquipo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valorCompraEquipo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.equipo

# --------------------------------------------------------------------------
class InsumoFinca(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=False)
    existenciaInsumo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valorUnitarioInsumo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return  self.insumo
# --------------------------------------------------------------------------
class CompraInsumo(models.Model):
    insumoFinca = models.ForeignKey(InsumoFinca, on_delete=models.CASCADE, null=False)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=False)
    fechaCompraInsumo = models.DateField(default= date.today)
    numFactura = models.CharField(max_length=20, null=False)
    cantidadCompraInsumo = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valorCompraInsumo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.insumo
# --------------------------------------------------------------------------
class Trabajador(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    nombreTrabajador = models.CharField(max_length=100, null=False)
    telefonoTrabajador = models.CharField(max_length=20, null=False)
    nitTrabajador = models.CharField(max_length=20, null=False)
    emailTrabajador = models.CharField(max_length=100, null=False)
    costoHoraTrabajador = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    rol = models.IntegerField(default=0)

    def __str__(self):
        return  self.nombreTrabajador

# --------------------------------------------------------------------------
class Producto(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)
    existenciaProducto = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descripProducto = models.CharField(max_length=200, null=False)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return  self.descripProducto
# --------------------------------------------------------------------------
class Cultivo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=False)
    fechaSiembra = models.DateField(default= date.today)
    fechaCosecha = models.DateField(default= date.today)
    cantidadCosecha= models.IntegerField(default= 0)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=False)
    observacCultivo = models.CharField(max_length=200, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return  self.producto

# --------------------------------------------------------------------------
class InsumosLabor(models.Model):
    insumoFinca = models.ForeignKey(InsumoFinca, on_delete=models.CASCADE, null=False)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=False)
    cantidadUsadaInsumo= models.IntegerField(default= 0)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.insumoFinca
# --------------------------------------------------------------------------
class EquiposLabor(models.Model):
    equipoFinca = models.ForeignKey(EquipoFinca, on_delete=models.CASCADE, null=False)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=False)
    cantidadUsadaEquipo= models.IntegerField(default= 0)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.equipoFinca

    class Meta():
        verbose_name_plural = 'Equipos Labores'
    


# --------------------------------------------------------------------------
class HorasTrabajo(models.Model):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=False)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=False)
    categHoras = models.ForeignKey(CategHoras, on_delete=models.CASCADE, null=False)
    observacLabor = models.CharField(max_length=200, null=True)
    tipoTrabajo = models.CharField(max_length=20, null=True)
    fechaLabor = models.DateField(default= date.today)
    duracionLabor = models.IntegerField(default= 0)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return  self.observacLabor
        
# --------------------------------------------------------------------------
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100, null=False)
    telefonoCliente = models.CharField(max_length=20, null=False)
    nitCliente = models.CharField(max_length=20, null=False)
    direccionCliente = models.CharField(max_length=200, null=False)
    correoCliente = models.CharField(max_length=100, null=False)
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombreCliente

# --------------------------------------------------------------------------
class Venta(models.Model):
    numFactura = models.CharField(max_length=20, null=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    fechaVenta = models.DateField(default= date.today)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    cantidadVenta = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valorTotalventa = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    observacVenta = models.CharField(max_length=200, null=True)

    def __str__(self):
        return  self.producto
