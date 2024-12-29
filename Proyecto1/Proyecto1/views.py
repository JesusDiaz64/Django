from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola Jesus Diaz")

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