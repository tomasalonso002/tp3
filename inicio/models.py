from django.db import models

# Create your models here.

class Consultas(models.Model):
    nombre =  models.CharField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    titulo_contenido = models.CharField(max_length=20)
    contenido = models.TextField(max_length=400)
    gmail = models.EmailField(max_length=30)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} - {self.titulo_contenido}"
