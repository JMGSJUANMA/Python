# App para invertir una frase ingresada por el usuario
frase = input("Ingrese una frase: ")  # Solicitar al usuario que ingrese una frase
frase_invertida = ""  # Variable para almacenar la frase invertida
indice = len(frase) - 1  # Índice para recorrer la frase de forma inversa

# Invertir la frase
while indice >= 0:
    frase_invertida += frase[indice]  # Agregar el carácter al inicio de la frase invertida
    indice -= 1  # Disminuir el índice para avanzar hacia el inicio de la frase
print(f"Frase invertida: {frase_invertida}")  # Mostrar la frase invertida

# Explicación del código:
# 1. Se solicita al usuario que ingrese una frase.
# 2. Se inicializa una variable frase_invertida como una cadena vacía.
# 3. Se calcula el índice inicial para recorrer la frase de forma inversa. El índice se calcula como la longitud de la frase menos 1, ya que los índices en Python comienzan en 0.
# 4. Se inicia un bucle while que se ejecutará mientras el índice sea mayor o igual a 0.
# 5. Dentro del bucle, se agrega el carácter correspondiente al índice actual al inicio de la frase_invertida.
# 6. Se disminuye el índice en 1 para avanzar hacia el inicio de la frase.
# 7. Una vez
# 8. Se muestra la frase invertida al usuario.

# Nota: Este código puede ser ejecutado en cualquier lenguaje de programación que soporte cadenas y bucles.
# Se puede adaptar a otros lenguajes cambiando la sintaxis específica de cada uno.

    