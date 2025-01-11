cantidad = 5
cantidad2 = 3

# for numero in range(cantidad):
#     for numero2 in range(cantidad2):
#         print(f"""
#               {numero}, {numero2}""")
        
        
# nombre = ["Juan", "Pedro", "Maria", "Jose", "Ana"]
# apellido = ["Perez", "Gomez", "Lopez", "Gonzalez", "Garcia"]

# for i in range(5):
#     print(f"{nombre[i]} {apellido[i]}")

# buscar = 7

# for i in range(9):
#     print(i)
#     if i == buscar:
#         print(f"Encontrado: {i}")
#         break
    
# for char in "hola":
#     print(char)
    
# numero = 1
# while numero < 100:
#     print(numero) 
#     numero *= 2

# comando = ""

# while comando.lower() != "salir":
#     comando = input("$")
#     print(f"Has introducido {comando}")
# print("""
#     Bienvenidos, Calculadora.
#     Para salir escribe salir...
#     Las operaciones disponibles son Suma, Resta, Multplicacion y Division.""")

# operacion = ""

# while operacion != "salir":
#     operacion = input("Ingrese que operacion desea realizar: ").lower()
    
#     print("")
#     n1 = int(input("Ingrese el primer numero: "))
#     n2 = int(input("Ingrese el segundo numero: "))
    
#     if operacion == "suma":
#         print(f"La suma de {n1} + {n2} es {n1 + n2}")
        
#     elif operacion == "resta":
#         print(f"La resta de {n1} - {n2} es {n1 - n2}")
    
#     elif operacion == "multiplicacion":
#         print(f"La multiplicacion de {n1} x {n2} es {n1 * n2}")
    
#     elif operacion == "division":
#         print(f"La division de {n1} / {n2} es {n1 / n2}")
#     elif operacion == "salir":
#         print("Saliendo de la calculadora...")
#         break
#     else:
#         print("Comando de operacion desconocido...")

# def suma(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     print(resultado)

# suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def resta(*numeros):
#     resultado = 0
#     for i in numeros:
#         resultado -= i
#     print(resultado)

# resta(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def multiplicacion(*numeros):
#     resultado = 0 
#     for i in numeros:
#         resultado *= i 
#     print(resultado)

# multiplicacion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def agenda(*nombres):
#     id = 0
#     for nombre in nombres:
#         print(f"{id}.{nombre}")
#         id += 1
#     print("Terminar ciclo...")

# agenda("Juan", "Pedro", "Maria", "Jose", "Ana")

# def productos_seleccionado(**datos):
#     print(f"""Estos son los productos que tomaste: 
#           id = {datos["id"]}
#           nombre = {datos["nombre"]}
#           descripcion = {datos["descripcion"]}
#           precio = {datos["precio"]}
#           cantidad = {datos["cantidad"]}
#           precio total = {datos["cantidad"] * datos["precio"]}
#           """)

# productos_seleccionado(id = 1,
#                        nombre = "Shampoo",
#                        descripcion = "Shampoo para cabello seco", 
#                        precio = 50,
#                        cantidad = 2)

# productos_seleccionado(id = 2,
#                        nombre = "Jabon en barra",
#                        descripcion = "Jabon para el cuerpo", 
#                        precio = 22,
#                        cantidad = 4)

# def largo(texto):
#     resultado = 0
#     for _ in texto:
#         resultado += 1
#         return resultado

# print("Chanchito")
# l = largo("Hola mundo")
# print(l)

def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto
    
def vuelta(texto):
    vuelta_texto = ""
    for char in texto:
        vuelta_texto = char + vuelta_texto
    return vuelta_texto

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = vuelta(texto)
    return texto == texto_al_reves
    
print(es_palindromo("anita lava la tina"))
print(es_palindromo("Hola mundo"))
        