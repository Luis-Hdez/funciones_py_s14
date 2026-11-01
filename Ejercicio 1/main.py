def calcular_renta(salario_bruto):
    """Calcula la deducción de renta (10% del salario bruto)."""
    return salario_bruto * 0.10

def calcular_salario_liquido(salario_bruto):
    """Invoca calcular_renta y devuelve una tupla con (salario_liquido, renta)."""
    renta = calcular_renta(salario_bruto)
    salario_liquido = salario_bruto - renta
    return salario_liquido, renta

def main():
    print("--- SISTEMA DE CÁLCULO DE PLANILLA ---")
    try:
        n = int(input("Ingrese la cantidad de empleados a registrar: "))
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    empleados = []
    total_liquidos = 0
    total_renta_retenida = 0

    for i in range(n):
        print(f"\n--- Empleado {i+1} ---")
        nombre = input("Nombre del empleado: ")
        
        while True:
            try:
                bruto = float(input("Salario bruto ($): "))
                if bruto < 0:
                    print("El salario no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido. Intente de nuevo.")
        
        # Invocamos la función que calcula líquido y renta (devuelve tupla)
        liquido, renta = calcular_salario_liquido(bruto)

        total_liquidos += liquido
        total_renta_retenida += renta

        # Almacenamos en una lista de diccionarios
        empleados.append({
            "nombre": nombre,
            "bruto": bruto,
            "liquido": liquido,
            "renta": renta
        })

    # Reporte final
    print("\n==============================================")
    print("             REPORTE FINAL DE PLANILLA        ")
    print("==============================================")
    for emp in empleados:
        print(f"Empleado: {emp['nombre']} | Bruto: ${emp['bruto']:.2f} | Líquido: ${emp['liquido']:.2f} | Renta: ${emp['renta']:.2f}")

    print("----------------------------------------------")
    print(f"Total pagado en salarios líquidos: ${total_liquidos:.2f}")
    print(f"Total de renta retenida:         ${total_renta_retenida:.2f}")



if __name__ == "__main__":
    main()
