import string 
import random

letters = list(string.ascii_letters.lower())
numbers = list(string.digits)
special = list("$@/!%&")

caracteres = list(letters + numbers + special)

tam = int(input("¿Cuál quieres que sea el tamaño de tu contraseña?: "))


if tam < 8 or tam > 20:
    print("Error! la constraseña debe tener entre 8 a 20 caracteres")
else:
    password = []

    password.append(random.choice(letters))
    password.append(random.choice(numbers))
    password.append(random.choice(special))

    for i in range(tam-3):
        password.append(random.choice(caracteres))

    random.shuffle(password)

    print("".join(password))