from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
# Create your views here.

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola Mundo, {fecha_hora_ahora}")

def pregunta(request, nombre):
    return HttpResponse(f"Hola, como estas {nombre.capitalize()}?")
