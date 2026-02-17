### Área de un polígono ###


"""
-Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""


tipo = input("¿Cuál es el área que quieres calcular la del cuadrado, triangulo o la del rectangulo?")
medidas = (input("Dime la medida (ej: 5) o medidas separadas por coma (ej: 10,5): "))

mi_poligono = [tipo, medidas]

def calcular_area(mi_poligono):
    if mi_poligono[0].lower().strip() == "cuadrado":
       area_cuadrado = float(mi_poligono[1])**2
       return area_cuadrado
    elif mi_poligono[0].lower().strip() == "triangulo":
        base_txt, altura_txt = mi_poligono[1].split(",")
        base_txt = float(base_txt)
        altura_txt = float(altura_txt)
        area_triangulo = ((base_txt*altura_txt)/2)
        return area_triangulo
    elif mi_poligono[0].lower().strip() == "rectangulo":
        base_txt, altura_txt = mi_poligono[1].split(",")
        base_txt = float(base_txt)
        altura_txt = float(altura_txt)
        area_rectangulo = (base_txt*altura_txt)
        return area_rectangulo
    else:
        return "Error: Polígono no reconocido"

resultado= calcular_area(mi_poligono)
print(resultado)


titulo = "Pruebas automáticas"
print(titulo.center(40,"-"))
print(f"Área cuadrado (lado 5): {calcular_area(["cuadrado", "5"])}")
print(f"Área triangulo (base 10, altura 5): {calcular_area(["triangulo", "10, 5"])}")
print(f"Área rectangulo (base 20, altura 4): {calcular_area(["rectangulo", "20, 4"])}")