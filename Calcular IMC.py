# Vamos hacer un ejercicio para calcular el IMC

peso = (int(input("¿Cual es tu peso actual en kg?")))
altura = float(input(("¿Cuanto es tu altura actual?")))

def imc():
    return (peso / altura**2)

print("{:.2f}".format(imc()))
resultado = imc()

if imc() < 18.5:
    print("Peso insuficiente")
elif imc() >= 18.5 and imc() < 24.9:
    print("Peso saludable")
elif imc() >= 24.9 and imc() < 29.9:
    print("Sobrepeso")
elif imc() >= 29.9 and imc() < 34.9:
    print("Obesidad")
else:
    print("Obesidad morbida")

