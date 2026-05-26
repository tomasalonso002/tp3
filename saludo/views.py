from django.http import HttpResponse
from django.shortcuts import render
from rutina.models import Rutina

def saludo (request):  
    rutinas = Rutina.objects.all()   
    return render(request, 'saludo/index.html', {"rutinas": rutinas}) 

def despedir (request):
    return render(request, 'saludo/despedir.html') 
