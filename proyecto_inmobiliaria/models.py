from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    TIPO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono_personal = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_CHOICES)


class Propiedad(models.Model):
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    )
    
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_totales = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES)
    precio_arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

