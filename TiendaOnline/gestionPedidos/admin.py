from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono") 
    # SE CREA UNA LISTA A LA CUAL SE MOSTRARA EN PANTALLA DEL ADMINISTRADOR.
    # LLAMAR LA CLASE A IMPRIMIR EN REGISTER PARA VISUALIZAR.
    
    search_fields = ("nombre", "telefono")
    #BUSQUEDA
    
class ArticulosAdmin(admin.ModelAdmin): # Filtro para productos dentro el panel de administracion
    list_filter = ("seccion",) # Esto es una tupla
    
class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha" # Pequeña pestaña de busqueda

admin.site.register(Clientes, ClientesAdmin) # AQUI.
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)

#....... ES UN REGISTRÓ PARA POSTGRESQL PARA QUE LO UTILICE EL ADMINISTRADOR.
#....... CREACIÓN DE TABLAS EN LA PAGINA DEL ADMINISTRADOR.