from django.db import models
from django.contrib.auth.models import User


class CategoriaRutina(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Rutina(models.Model):

    NIVEL_CHOICES = [
        ('PRI', 'Principiante'),
        ('INT', 'Intermedio'),
        ('AVA', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    series = models.PositiveIntegerField(default=3)
    repeticiones = models.PositiveIntegerField(default=10)

    tiempo_descanso = models.PositiveIntegerField(
        help_text="Tiempo de descanso en segundos",
        default=60
    )

    nivel = models.CharField(
        max_length=3,
        choices=NIVEL_CHOICES,
        default='PRI'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    entrenador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rutinas"
    )

    categorias = models.ManyToManyField(
        CategoriaRutina,
        blank=True,
        related_name="rutinas"
    )

    activa = models.BooleanField(default=True)

    imagen = models.ImageField(
        upload_to='rutinas/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre