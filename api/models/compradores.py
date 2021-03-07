from django.db import models
from django.contrib.auth.models import AbstractUser


class Compradores(AbstractUser):
    nombre=models.CharField('Nombre',max_length=255)
    apellido=models.CharField('Apellido',max_length=255)
    direccion=models.CharField('Direccion',max_length=255)
    ciudad=models.CharField('Ciudad',max_length=255)
    longitud=models.CharField('Longitud',max_length=255)
    latitud=models.CharField('Latitud',max_length=255)
    estado_geo=models.CharField('Estado geo',max_length=255)
    REQUIRED_FIELDS=["nombre","apellido","direccion"]

    class Meta:
        verbose_name="Comprador"
        verbose_name_plural="Compradores"

    def __str__(self):
        return "{}. {} {}".format(self.pk,self.nombre,self.apellido)