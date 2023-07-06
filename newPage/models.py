from django.db import models

# Create your models here.


    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apPaterno = models.CharField(max_length=50, blank=False, null=False)
    apMaterno = models.CharField(max_length=50, blank=False, null=False)
    correo = models.EmailField(max_length=60, blank=False, null = False, primary_key=True)
    contraseña = models.CharField(max_length=50, blank=False, null=False)
    confirmar_contraseña = models.CharField(max_length=50, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return str(self.nombre)+" "+str(self.apPaterno)+" "+str(self.apMaterno)


class Productos(models.Model):
    codigo =    models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50,blank=False, null=False )
    precio = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.codigo)+" "+str(self.nombre)+" "+str(self.precio)