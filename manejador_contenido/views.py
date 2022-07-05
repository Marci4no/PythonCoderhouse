from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, "manejador_contenido/base.html", {})

def mostrar_profile(request):
    return render(request, "manejador_contenido/base.html", {})