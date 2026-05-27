from django import forms
from .models import Rutina, CategoriaRutina

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ['nombre', 'categoria', 'descripcion']