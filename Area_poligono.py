def calcular_area_poligono(tipo, *args):
    """
    Calcula y devuelve el área de un polígono dado.

    Parámetros:
        - tipo: Tipo de polígono ('triangulo', 'cuadrado' o 'rectangulo').
        - *args: Argumentos necesarios para calcular el área del polígono.
          Para el triángulo: base y altura.
          Para el cuadrado: lado.
          Para el rectángulo: base y altura.
    """
    if tipo.lower() == 'triangulo':
        base, altura = args
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif tipo.lower() == 'cuadrado':
        lado = args[0]
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    elif tipo.lower() == 'rectangulo':
        base, altura = args
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    else:
        print("Tipo de polígono no soportado.")

    return area

# Ejemplos de uso
calcular_area_poligono('triangulo', 5, 8)
calcular_area_poligono('cuadrado', 4)
calcular_area_poligono('rectangulo', 6, 9)
