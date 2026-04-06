### Día 3 ###

#Palindromos
variable_1: str = input("¿Qué palabra quieres saber si es un palindromo?")
variable_1 = variable_1.lower()

variable_2 = list(variable_1)


variable_3 = list(reversed(variable_2))


while " " in variable_2:
    variable_2.remove(" ")

while " " in variable_3:
    variable_3.remove(" ")

if variable_2 == variable_3:
    print("si es un palindromo")
else:
    print("no es un palindromo")


