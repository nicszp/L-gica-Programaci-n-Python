### Invirtiendo cadenas ###

"""

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.

 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

cadena_de_texto = input("¿Qué palabra quieres invertirle el orden ?")

texto_invertido = ""

for letra in cadena_de_texto:
    texto_invertido = letra + texto_invertido

resultado = texto_invertido
print(f"La palabra de manera invertida es: {resultado}")





