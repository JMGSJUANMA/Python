def es_palindromo(cadena):
    """Función que verifica si una cadena es un palíndromo."""
    cadena = cadena.lower()  # Convertir la cadena a minúsculas
    i = 0
    d = len(cadena) - 1
    while d > i:
        if cadena[i] != cadena[d]:
            return False
        i += 1
        d -= 1
    return True


def solo_letras(cadena):
    """Función que verifica si la cadena contiene solo letras."""
    return cadena.isalpha()


# Mensaje inicial
print("Ingrese las palabras que desee.")
print("Cuando ya no quiera ingresar más, escriba 'fin'.")

cantidad_palindromos = 0  # Contador de palíndromos
palindromos = []  # Lista para almacenar los palíndromos
cadena = input("\nCadena: ")

# Bucle principal
while cadena.lower() != "fin":  # Convertir a minúsculas para comparación
    if not solo_letras(cadena):  # Validar que solo contenga letras
        print("Error: Solo se permiten letras. Inténtelo de nuevo.")
    elif es_palindromo(cadena):  # Verificar si es un palíndromo
        cantidad_palindromos += 1
        palindromos.append(cadena)  # Agregar a la lista de palíndromos
    cadena = input("Cadena: ")

# Resultados
print("\nCantidad de palíndromos:", cantidad_palindromos)
if cantidad_palindromos > 0:
    print("Palíndromos encontrados:", ", ".join(palindromos))
else:
    print("No se encontraron palíndromos.")
