from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuarioPersonalizadoForm, EditarUsuarioPersonalizadoForm
from django.contrib.auth.models import Group
from .models import UsuarioPersonalizado
# Create your views here.

@login_required
def nuevo_usuario(request):
    roles =  Group.objects.all()
    if request.method == "POST":
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_usuarios')
    else:
        form= UsuarioPersonalizadoForm()
    contexto = {
        'form':form,
        'roles':roles
    }
    return render(request,'usuarios/nuevo_usuario.html',contexto)

@login_required
def get_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.filter(is_active = True).order_by("-id")
    return render(request, 'usuarios/get_usuarios.html',{'usuarios':usuarios})


@login_required
def borrar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id = id)
    if request.method =="POST":
        usuario.is_active = False
        usuario.save()
        return redirect('get_usuarios')
    return render(request, 'usuarios/get_usuarios.html')


@login_required
def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioPersonalizado, id = id)
    if request.method == 'POST':
        form = EditarUsuarioPersonalizadoForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("get_usuarios")
    else:
        form = EditarUsuarioPersonalizadoForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html',{"form":form})
