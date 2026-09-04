# ==============================================================================
# Tarea: Reserva de un asiento en sala de cine
# Descripción: Programa en Python que gestiona una matriz de 3 filas por 4 columnas 
#              para la reserva de asientos (0 = libre, 1 = reservado).
# ==============================================================================

def main():
    # 1. Creación de la matriz de 3 filas por 4 columnas llamada 'asientos' inicializada en 0
    asientos = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    print("--- ESTADO INICIAL DE LA SALA ---")
    # Mostrar la matriz inicial usando bucles anidados
    for fila in range(len(asientos)):
        for col in range(len(asientos[fila])):
            print(asientos[fila][col], end=" ")
        print() # Salto de línea al terminar cada fila
    print("-" * 33)

    # 2. Solicitar al usuario la fila y la columna del asiento que desea reservar
    # Nota: Las filas válidas son 0, 1 y 2; las columnas válidas son 0, 1, 2 y 3.
    try:
        fila_usuario = int(input("Ingrese la fila que desea reservar (0 a 2): "))
        columna_usuario = int(input("Ingrese la columna que desea reservar (0 a 3): "))
        
        # Validar opcionalmente que los rangos sean correctos y el asiento esté libre
        if 0 <= fila_usuario < 3 and 0 <= columna_usuario < 4:
            if asientos[fila_usuario][columna_usuario] == 0:
                # 3. Marcar ese asiento como reservado asignándole el valor 1
                asientos[fila_usuario][columna_usuario] = 1
                print("\n¡Asiento reservado con éxito!")
            else:
                print("\nAviso: El asiento seleccionado ya se encuentra reservado.")
        else:
            print("\nError: La fila o la columna ingresada está fuera del rango permitido.")
            return
    except ValueError:
        print("\nError: Debe ingresar valores numéricos enteros válidos.")
        return

    # 4. Mostrar la matriz completa actualizada en formato de tabla utilizando bucles anidados
    print("\n--- ESTADO ACTUALIZADO DE LA SALA ---")
    for fila in range(len(asientos)):
        for col in range(len(asientos[fila])):
            print(asientos[fila][col], end=" ")
        print() # Salto de línea al terminar cada fila
    print("-" * 37)

if _ _name_ _ == "_ _main_ _":
    main()