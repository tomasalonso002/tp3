from django.contrib import admin
from .models import Rutina, CategoriaRutina

# Register your models here.

admin.site.register(CategoriaRutina)
admin.site.register(Rutina)