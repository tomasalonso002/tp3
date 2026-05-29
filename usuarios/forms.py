from django import forms
from .models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm


class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
<<<<<<< HEAD
        fields = UserCreationForm.Meta.fields + ('telefono','dni','foto_perfil')

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
            'password1',
            'password2',
        ]
=======
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','telefono','dni','email','foto_perfil')

class EditarUsuarioPersonalizadoForm(forms.ModelForm):
    class Meta:
        model= UsuarioPersonalizado
        fields=['username','first_name', 'last_name', 'telefono','email', 'foto_perfil']
>>>>>>> main
