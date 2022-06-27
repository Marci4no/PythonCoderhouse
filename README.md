# PythonCoderhouse
Repositorio dedicado al curso de python de coderhouse

## -- Instalacion y configuración Django -- ##

- 1) Instalar Django: pip install django
- 2) Configurar Django: (python -M) django-admin startproject #NombreDelProjecto -- mi_mvt en este caso
- 3) Migracion Django: python manage.py migrate
- 4) Configurar vistas y apps: python manage.py startapps
- 5) Iniciar el servidor: python manage.py runserver (ejecutar siempre que quieras visualizar la pagina web)

## -- Vistas (mi_apps/views.py) & URLS (mi_mvt/urls.py) -- ##

En views.py se configuran las vistas que mostrara la pagina web al momento de llamar alguna funcion
En urls.py se configura el ruteo de las vistas.

