from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        
        self.apellido = apellido
        
class Agenda_Persona(object):
    def __init__(self, nombre, apellidos, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono

def saludo(request):
    p1 = Persona("Jesus David", "Diaz Cabrales")
    
    # nombre = "Jesus"
    
    # apellido = "Diaz"
    
    temasCurso = []
    
    ahora = datetime.datetime.now()
    
    doc_externo = open("C:/Users/jdiaz/OneDrive/Documentos/Programacion/Django/Proyecto1/Proyecto1/plantillas/miPlantilla.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "hora" : ahora, "temas": temasCurso})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def materias(request):
    return HttpResponse("""Estas son las materias reprobadas
                        Matematicas: 69
                        Ingles: 54
                        Frances: 34
                        """)

def fecha(request):
    fecha_actual = datetime.datetime.now()
    
    documento = """
    <html>
    <body>
    <h1>
    
    Fecha y hora actuales: %s
    
    </h1>
    </body>
    </html>
    """ % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual = 18
    periodo = agno - 2019
    edadFutura = edadActual + periodo
    documento = "<html><body><h2> En el año %s tendrás %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)

def agenda_telefono(request):
    agenda1 = Agenda_Persona("Edgar Yoel", "Diaz Cabrales", 6644714104)
    
    doc_externo = open("C:/Users/jdiaz/OneDrive/Documentos/Programacion/Django/Proyecto1/Proyecto1/plantillas/plantillaAgenda.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context({"Nombre_agendado": agenda1.nombre, "Apellido_agendado": agenda1.apellidos, "Telefono_agendado": agenda1.telefono})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)