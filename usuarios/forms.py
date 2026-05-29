from django import forms
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm


# 1. Formulario de creación (Campos unificados de Maxi y Tomás)
class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'telefono', 'dni', 'email', 'foto_perfil')


# 2. Tu formulario de registro público (Maxi)
class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = [
            'username',
            'email',
            'telefono',
            'dni',
            'fecha_nacimiento',
            'foto_perfil',
        ]


# 3. Formulario de edición (Tomás)
class EditarUsuarioPersonalizadoForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'first_name', 'last_name', 'telefono', 'email', 'foto_perfil']