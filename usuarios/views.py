from django.shortcuts import render, redirect
from .forms import UsuarioPersonalizadoForm
# Create your views here.
def nuevo_usuarios(request):
    if request.method == "POST":
        print(request.FILES)
        form = UsuarioPersonalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form= UsuarioPersonalizadoForm()
    return render(request,'usuarios/usuarios.html',{'form':form})