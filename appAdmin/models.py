from django.db import models

# Create your models here.

#------------------------------------------------
class CategMaterial(models.Model):
    descripCategMaterial = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.descripCategMaterial

    class Meta:
        verbose_name_plural = "Categorias de Material y equipo"

#------------------------------------------------
class UnidadMedida(models.Model):
    descripUnidadMedida = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.descripUnidadMedida

    class Meta:
        verbose_name_plural = "Unidades de medida"

#------------------------------------------------
class CategHoras(models.Model):
    descripCategHora = models.CharField(max_length=100, null=False)
    recargo = models.DecimalField(max_digits=4, decimal_places=2, default= 1.00)

    def __str__(self):
        return str(self.id) + ' ' + self.descripCategHora
        
    class Meta:
        verbose_name_plural = "Categorias de Horas"

#------------------------------------------------
class Equipo(models.Model):
    categMaterial = models.ForeignKey(CategMaterial, on_delete=models.CASCADE, null=False)
    descripEquipo = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.descripEquipo

#------------------------------------------------
class Insumo(models.Model):
    categMaterial = models.ForeignKey(CategMaterial, on_delete=models.CASCADE, null=False)
    descripInsumo = models.CharField(max_length=100, null=False)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.descripInsumo
#------------------------------------------------
class Proveedor(models.Model):
    telefonoProveedor = models.IntegerField( null=True)
    nombreProveedor = models.CharField(max_length=100, null=False)
    nitProveedor = models.CharField(max_length=20, null=False)
    direccionProveedor = models.CharField(max_length=200, null=False)
    correoProveedor = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombreProveedor

    class Meta:
        verbose_name_plural = "Proveedores"
#------------------------------------------------