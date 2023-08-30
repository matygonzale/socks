from django.db import models
from modulo.usuarios.models import *
from django.contrib.auth.models import User

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    
    
    

class Ventas(models.Model):
    monto = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.DateTimeField()
    idCliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    idVendedor = models.ForeignKey(Vendedor, models.DO_NOTHING)
    idProducto = models.ForeignKey(Producto, models.DO_NOTHING)
    
    def __str__(self):
        return self.id
    

