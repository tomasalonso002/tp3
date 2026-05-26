from django import forms
from .models import Consultas

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = ["nombre", "titulo_contenido", "contenido", "gmail","telefono"]
    