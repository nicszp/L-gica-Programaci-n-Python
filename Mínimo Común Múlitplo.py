
# Mínimo común múltiplo

def mcm(valor_1,valor_2):
    if valor_1 > valor_2:
        valor_mayor = valor_1
    else:
        valor_mayor = valor_2

    while (valor_mayor % valor_1) != 0 or (valor_mayor % valor_2) != 0:
        valor_mayor += 1
        
    return valor_mayor

print(mcm(8,21))

