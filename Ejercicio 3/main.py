def evaluar_aspirante(nombre, *notas):
    """Recibe un nombre y una cantidad variable de notas usando *args."""
    if not notas:
        promedio = 0.0
    else:
        promedio = sum(notas) / len(notas)

    if promedio >= 7.0:
        estado = "Admitido"
    else:
        estado = "No Admitido"

    # Retorna un diccionario con los datos procesados
    return {
        "nombre": nombre,
        "promedio": promedio,
        "estado": estado
    }

def main():
    print("--- SISTEMA DE ADMISIÓN DE ASPIRANTES ---")
    
    # 1. Bucle para asegurar una cantidad válida de aspirantes
    while True:
        try:
            n_aspirantes = int(input("¿Cuántos aspirantes desea evaluar?: "))
            if n_aspirantes <= 0:
                print("Debe evaluar al menos a 1 aspirante.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    aspirantes_registrados = []
    total_admitidos = 0

    for i in range(n_aspirantes):
        print(f"\n--- Aspirante {i+1} ---")
        nombre = input("Nombre del aspirante: ")
        
        # 2. Bucle para ingresar notas una por una hasta que escriban 'salir'
        lista_notas = []
        print("Ingrese las notas una por una. Escriba 'salir' para terminar con este aspirante.")
        
        while True:
            entrada = input("Ingrese nota: ")
            
            # Si el usuario quiere terminar
            if entrada.lower() == 'salir':
                if not lista_notas:
                    print("Error: Debe ingresar al menos una nota antes de salir.")
                    continue
                break # Salimos del bucle de notas
            
            try:
                # Convertimos lo ingresado a float
                nota = float(entrada)
                
                # Validación de rango (asumiendo escala de 0 a 10)
                if nota < 0 or nota > 10:
                    print("Error: La nota debe estar en el rango de 0 a 10.")
                    continue
                
                # Si es válida, la agregamos a la lista
                lista_notas.append(nota)
                
            except ValueError:
                print("Error: Ingrese un número válido o la palabra 'salir'.")

        # 3. Llamamos a la función usando *args (desempaquetando la lista)
        # 3. Procesamiento seguro de los datos del aspirante actual
        resultado = evaluar_aspirante(nombre, *lista_notas)
        aspirantes_registrados.append(resultado)

        if resultado["estado"] == "Admitido":
            total_admitidos += 1

    # Reporte final de admisiones
    print("\n==============================================")
    print("           RESULTADOS DE ADMISIÓN             ")
    print("==============================================")
    for asp in aspirantes_registrados:
        print(f"Aspirante: {asp['nombre']} | Promedio: {asp['promedio']:.2f} | Veredicto: {asp['estado']}")

    print("----------------------------------------------")
    print(f"Cantidad total de aspirantes admitidos: {total_admitidos}")

if __name__ == "__main__":
    main()
