from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UsuarioPersonalizadoForm
from .models import UsuarioPersonalizado
# Create your views here.

@login_required
def nuevo_usuario(request):
    if request.method == "POST":
        print(request.FILES)
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= UsuarioPersonalizadoForm()
    return render(request,'usuarios/nuevo_usuario.html',{'form':form})

@login_required
def get_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.filter(is_active = True).order_by("-id")
    return render(request, 'usuarios/usuarios.html',{'usuarios':usuarios})