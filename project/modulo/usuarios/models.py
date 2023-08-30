from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    correo = models.CharField(primary_key=True, max_length=100)
    Run = models.PositiveIntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.PositiveBigIntegerField()
    idUser = models.OneToOneField(User, models.CASCADE)
    
    def __str__(self):
        return self.nombre +' '+ self.apellido
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    