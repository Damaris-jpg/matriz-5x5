# Programa: reserva_cine.py
# Descripción: Gestión de reservas de asientos para una sala de cine (3 filas y 4 columnas).
# 0 = asiento libre, 1 = asiento reservado

# 1. Crear matriz de 3 filas por 4 columnas inicializada en 0
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("--- ESTADO INICIAL DE LA SALA DE CINE ---")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

print("\n--- REALIZAR RESERVA ---")
# 2. Solicitar al usuario la fila y la columna
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# Validar que los datos estén dentro del rango permitido
if 0 <= fila < 3 and 0 <= columna < 4:
    if asientos[fila][columna] == 0:
        # 3. Marcar el asiento como reservado asignando el valor 1
        asientos[fila][columna] = 1
        print("\n¡Asiento reservado exitosamente!")
    else:
        print("\nEl asiento seleccionado ya se encontraba reservado.")
else:
    print("\nError: La fila o columna ingresada está fuera de rango.")

# 4. Mostrar el estado completo de la sala en formato de tabla usando bucles anidados
print("\n--- ESTADO ACTUALIZADO DE LA SALA ---")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()