# Separamos la lógica de operaciones en un archivo aparte llamado operaciones.py
# De esta manera, podemos importar este módulo en otros archivos y reutilizar las funciones definidas aquí.
# Definimos funciones para realizar operaciones matemáticas básicas.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def multiplicar(a, b):
    return a * b

def es_par(numero):
    return numero % 2 == 0