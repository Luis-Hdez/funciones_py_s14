def calcular_total_producto(precio, cantidad, impuesto=0.13):
    """Calcula el subtotal con impuestos utilizando un argumento por defecto para el IVA (13%)."""
    subtotal = precio * cantidad
    total_con_impuesto = subtotal + (subtotal * impuesto)
    return total_con_impuesto

def aplicar_descuento_especial(total, porcentaje_descuento=5):
    """Aplica un descuento si el total supera los $100.00 usando un argumento por defecto (5%)."""
    if total > 100.0:
        descuento = total * (porcentaje_descuento / 100.0)
        return total - descuento
    return total

def main():
    print("--- SISTEMA DE FACTURACIÓN EN LÍNEA ---")
    productos = []

    while True:
        nombre = input("\nNombre del producto (o escriba 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        # 1. Bucle exclusivo para validar el PRECIO
        while True:
            try:
                precio = float(input("Precio unitario ($): "))
                if precio < 0:
                    print("El precio debe ser un valor positivo.")
                    continue
                break # Precio correcto, avanzamos al siguiente dato
            except ValueError:
                print("Error: Por favor ingrese un número válido para el precio.")

        # 2. Bucle exclusivo para validar la CANTIDAD
        while True:
            try:
                cantidad = int(input("Cantidad comprada: "))
                if cantidad < 0:
                    print("La cantidad debe ser un valor positivo.")
                    continue
                break # Cantidad correcta, salimos de las validaciones
            except ValueError:
                print("Error: Por favor ingrese un número entero válido para la cantidad.")

        # 3. Procesamiento y guardado seguro del producto
        total_parcial = calcular_total_producto(precio, cantidad)

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "total_parcial": total_parcial
        })
        print("Producto agregado al carrito.")

    if not productos:
        print("\nNo se registraron compras.")
        return

    # Cálculo general de la compra
    subtotal_general = sum(p["total_parcial"] for p in productos)
    
    # Aplicar descuento especial si supera los $100
    total_final = aplicar_descuento_especial(subtotal_general)

    # Ticket de compra
    print("\n==============================================")
    print("               TICKET DE COMPRA               ")
    print("==============================================")
    for p in productos:
        print(f"- {p['nombre']} (Cant: {p['cantidad']}) | Total c/ IVA: ${p['total_parcial']:.2f}")
    
    print("----------------------------------------------")
    print(f"Subtotal general:              ${subtotal_general:.2f}")
    if subtotal_general > 100.0:
        print("¡Descuento especial aplicado! (5%)")
    print(f"TOTAL A PAGAR:                 ${total_final:.2f}")

if __name__ == "__main__":
    main()
