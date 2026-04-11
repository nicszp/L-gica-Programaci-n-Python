# Eliminar los duplicados de una lista

fname = input("¿Cual es tu nombre?")

def greetings(fname):
    print(f"Welcome to my program {fname}")ç

greetings(fname)

lista = [2, 23, 34, 37, 34, 65, 78, 90, 1,23, 37, 56, 80, 99, 10, 11, 24, 56, 66, 80, 99]
lista_vacia = []
lista_duplicados = []

for num in lista:
    if num not in lista_vacia:
        lista_vacia.append(num)
    else:
        lista_duplicados.append(num)

print(f"Esta es la lista con los números sin duplicar: {lista_vacia}")
print(f"Esta es la lista con los números duplicados: {lista_duplicados}")