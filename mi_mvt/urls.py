from django.contrib import admin
from django.urls import path
from mi_app.views import listar_cursos, listar_estudiantes, listar_familiares, mostrar_index, saludo, pregunta, saludo_personalizado


urlpatterns = [
    path('saludar/', saludo),
    path('saludar/persona/<nombre>', pregunta),
    path('saludo-personalizado/', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('listar-familiares/', listar_familiares),
    path('inicio/', mostrar_index)
]
