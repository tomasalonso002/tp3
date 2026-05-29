from django import forms
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm


class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','telefono','dni','email','foto_perfil')

class EditarUsuarioPersonalizadoForm(forms.ModelForm):
    class Meta:
        model= UsuarioPersonalizado
        fields=['username','first_name', 'last_name', 'telefono','email', 'foto_perfil']