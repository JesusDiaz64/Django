from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        
        self.apellido = apellido
        
class Agenda_Persona(object):
    def __init__(self, nombre, apellidos, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono

class Calculadora(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.suma = num1 + num2
        self.resta = num1 - num2
        self.multiplicacion = num1 * num2
        self.division = num1 / num2

def saludo(request):
    p1 = Persona("Jesus David", "Diaz Cabrales")
    
    # nombre = "Jesus"
    
    # apellido = "Diaz"
    
    temasCurso = ["Matematicas", "Ingles", "Frances", "Programacion"]
    
    ahora = datetime.datetime.now()
    
    #Ver settings...
    #plt = get_template("miplantilla.html")
    
    #ctx = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "hora" : ahora, "temas": temasCurso})
    
    #documento = plt.render({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "hora" : ahora, "temas": temasCurso})
    
    return render(request, "miplantilla.html", {"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "hora" : ahora, "temas": temasCurso})

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
    
    plt = get_template("plantillaAgenda.html")
    
    documento = plt.render({"Nombre_agendado": agenda1.nombre, "Apellido_agendado": agenda1.apellidos, "Telefono_agendado": agenda1.telefono})
    
    return HttpResponse(documento)

def calculadora(request):
    Calcular = Calculadora(45, 5)
    
    plt = get_template("calPlantilla.html")
        
    documento = plt.render({"Primer_numero": Calcular.num1, "Segundo_numero": Calcular.num2, "Suma": Calcular.suma, "Resta": Calcular.resta, "Multiplicacion": Calcular.multiplicacion, "Division": Calcular.division})
    
    return HttpResponse(documento)