from django.db import models

# Create your models here.


    
# Modelo de cliente, con sus campos de datos correspondientes
class Cliente(models.Model):
    correo = models.EmailField(max_length=60, blank=False, null = False, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=50, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    contraseña = models.CharField(max_length=50, blank=False, null=False)
    confirmar_contraseña = models.CharField(max_length=50, blank=False, null=False)