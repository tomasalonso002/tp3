from django import forms
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm


class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('telefono','dni','foto_perfil')