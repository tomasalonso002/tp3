from django.shortcuts import render, redirect
from .forms import UsuarioPersonalizadoForm, UsuarioRegistroForm
from django.contrib.auth import login


# Create your views here.

def nuevo_usuarios(request):

    if request.method == "POST":

        print(request.FILES)

        form = UsuarioPersonalizadoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('usuarios')

    else:

        form = UsuarioPersonalizadoForm()

    return render(
        request,
        'usuarios/usuarios.html',
        {'form': form}
    )


def register(request):

    if request.method == 'POST':

        form = UsuarioRegistroForm(
            request.POST,
            request.FILES
        )

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