from django.shortcuts import render,redirect
from .forms import ConsultasForm

# Create your views here.
def inicio(request):
    return render(request, "inicio/index.html")

def consultas(request):
    if request.method == "POST":
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            form = ConsultasForm()
            redirect("inicio")
    else:
        form = ConsultasForm()
    return render(request, "inicio/consultas.html", {"form":form})
