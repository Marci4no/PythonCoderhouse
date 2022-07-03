from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Familia
# Create your views here.

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola Mundo, {fecha_hora_ahora}")

def pregunta(request, nombre):
    return HttpResponse(f"Hola, como estas {nombre.capitalize()}?")

def saludo_personalizado(request):
    context = {}
    if request.GET:
        context["nombre"] = request.GET["nombre"]
    return render(request, "html\index.html", context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all()
    return render(request, "html\listar_cursos.html", context)

def listar_familiares(request):
    context = {}
    context["familiares"] = Familia.objects.all()
    return render(request, "html\listar_familiares.html", context)