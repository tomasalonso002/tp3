from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import UsuarioPersonalizado
from .forms import UsuarioPersonalizadoForm, UsuarioRegistroForm, EditarUsuarioPersonalizadoForm

# Create your views here.

# 1. Vista de creación (Versión de Tomás, consistente con las nuevas URLs)
@login_required
def nuevo_usuario(request):
    roles = Group.objects.all()
    if request.method == "POST":
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_usuarios')
    else:
        form = UsuarioPersonalizadoForm()
    
    contexto = {
        'form': form,
        'roles': roles
    }
    return render(request, 'usuarios/nuevo_usuario.html', contexto)


# 2. Tu vista de Registro Público (Maxi)
def register(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('rutinas')
    else:
        form = UsuarioRegistroForm()

    return render(
        request,
        'usuarios/register.html',
        {'form': form}
    )


# 3. Vistas de Gestión de Tomás (Listar, Borrar, Editar)
@login_required
def get_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.filter(is_active=True).order_by("-id")
    return render(request, 'usuarios/get_usuarios.html', {'usuarios': usuarios})


@login_required
def borrar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=id)
    if request.method == "POST":
        usuario.is_active = False
        usuario.save()
        return redirect('get_usuarios')
    return render(request, 'usuarios/get_usuarios.html')


@login_required
def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id=id)
    if request.method == 'POST':
        form = EditarUsuarioPersonalizadoForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("get_usuarios")
    else:
        form = EditarUsuarioPersonalizadoForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {"form": form})