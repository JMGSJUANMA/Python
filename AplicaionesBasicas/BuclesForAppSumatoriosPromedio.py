# Inicialización de variables
numeros = []  # Lista para almacenar los números ingresados
suma_negativos = 0  # Acumulará la suma de los números negativos
positivos = []  # Lista para almacenar los números positivos

# Solicitar al usuario que ingrese 6 números
for i in range(6):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)  # Agregar el número a la lista
    if numero < 0:
        suma_negativos += numero  # Sumar si el número es negativo
    elif numero > 0:
        positivos.append(numero)  # Agregar a la lista de positivos si es positivo

# Calcular el promedio de los positivos (si hay alguno)
if len(positivos) > 0:
    promedio_positivos = sum(positivos) / len(positivos)
else:
    promedio_positivos = 0  # Asignar 0 si no hay números positivos

# Mostrar resultados
print("\nResultados:")
print(f"Suma de los números negativos: {suma_negativos}")
if len(positivos) > 0:
    print(f"Promedio de los números positivos: {promedio_positivos:.2f}")
else:
    print("No se ingresaron números positivos, por lo que no hay promedio.")
