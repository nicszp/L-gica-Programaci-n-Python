# Separando pares e impares

# Vamos hacer un ejercicio donde vamos a seperar los números pares de los imparesxº

def separar_pares_impares(lista_numeros):
    
    pares = []
    impares = []

    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares

mi_lista = [20, 3, 4, 23, 45, 2, 52, 67, 89, 90, 1, 2, 34, 18, 84, 100]

pares, impares = separar_pares_impares(mi_lista)

pares.sort()
impares.sort()

print(f"Esta es la lista: {mi_lista}")
print(f"Estos son los números pares de la lista: {pares}")
print(f"Estos son los números impares de la lista: {impares}")