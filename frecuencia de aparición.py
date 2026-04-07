### Frecuencia de aparición ###

# Vamos a ver cuantas apariciones tiene cada caracter en una cadena

cadena = input("¿Cual es la cadena que quieres contar el numero de caracteres?")
cadena = cadena.lower()

caracteres = {}

for caracter in cadena:
    if cadena in caracteres:
        caracteres[caracter] += 1
    else:
        caracteres[caracter] = 1

print(caracteres)
