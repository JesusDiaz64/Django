from django.contrib import admin
from gestionContactos.models import Usuario, administrador

# Register your models here.

admin.site.register(Usuario)
admin.site.register(administrador)