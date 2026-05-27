from django.db import models
from django.contrib.auth.models import User


class CategoriaRutina(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaRutina, on_delete=models.CASCADE, blank=True)
    activa = models.BooleanField(default=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    