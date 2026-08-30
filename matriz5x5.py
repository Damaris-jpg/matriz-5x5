# Inicialización de la matriz de 5 filas por 5 columnas
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Lectura de datos desde la consola
print("--- Ingreso de datos ---")
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

# Impresión de la matriz ingresada
print("\n--- Matriz ingresada ---")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()
    