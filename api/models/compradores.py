from django.db import models
from django.contrib.auth.models import AbstractUser


class Compradores(AbstractUser):
    nombre=models.CharField('Nombre',max_length=255)
    apellido=models.CharField('Apellido',max_length=255)
    email=models.CharField('email',max_length=255,blank=True,null=True)
    direccion=models.CharField('Direccion',max_length=255)
    ciudad=models.CharField('Ciudad',max_length=255)
    longitud=models.CharField('Longitud',max_length=255,null=True,blank=True)
    latitud=models.CharField('Latitud',max_length=255,null=True,blank=True)
    estado_geo=models.CharField('Estado geo',max_length=255,null=True,blank=True)
    
    is_deleted=models.BooleanField(default=False)
    REQUIRED_FIELDS=["nombre","apellido","direccion","ciudad"]

    class Meta:
        verbose_name="Comprador"
        verbose_name_plural="Compradores"

    def __str__(self):
        return "{}. {} {}".format(self.pk,self.nombre,self.apellido)

    