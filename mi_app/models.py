from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    cursada= models.IntegerField()

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    parentezco = models.CharField(max_length=40)

