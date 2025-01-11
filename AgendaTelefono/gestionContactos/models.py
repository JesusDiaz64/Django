from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=80)
    

class administrador(models.Model):
    nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)