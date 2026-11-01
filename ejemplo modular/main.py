# Importamos el módulo operaciones.py para poder usar sus funciones
# Podemos importar una función específica usando: from nombre_archivo import nombre_funcion
# from operaciones import sumar, es un ejemplo de cómo importar una función específica, pero en este caso importaremos todo el módulo.

import operaciones

print("--- INICIANDO EL PROGRAMA PRINCIPAL ---")

# Usamos la función del otro archivo usando: nombre_archivo.funcion()

# Le pedimos al usuario que ingrese dos números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Probamos cada una de las funciones del módulo operaciones.py
resultado_suma = operaciones.sumar(a, b)
print(f"El resultado de la suma es: {resultado_suma}")

resultado_resta = operaciones.restar(a, b)
print(f"El resultado de la resta es: {resultado_resta}")

resultado_div = operaciones.dividir(a, b)
print(f"El resultado de la división es: {resultado_div}")

resultado_multi = operaciones.multiplicar(a, b)
print(f"El resultado de la multiplicación es: {resultado_multi}")

# Probando otra función del módulo
numero_prueba = a
if operaciones.es_par(numero_prueba):
    print(f"El número {numero_prueba} es par.")
else:
    print(f"El número {numero_prueba} es impar.")