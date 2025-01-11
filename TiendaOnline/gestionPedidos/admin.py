from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)

#....... ES UN REGISTRÓ PARA POSTGRESQL PARA QUE LO UTILICE EL ADMINISTRADOR.
#....... CREACIÓN DE TABLAS EN LA PAGINA DEL ADMINISTRADOR.