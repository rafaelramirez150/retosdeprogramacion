def es_anagrama(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas entre sí.
    """
    # Convertir las palabras a minúsculas y eliminar espacios en blanco
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    # Verificar si tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False

    # Contar la frecuencia de cada letra en ambas palabras
    contador_palabra1 = {}
    contador_palabra2 = {}

    for letra in palabra1:
        contador_palabra1[letra] = contador_palabra1.get(letra, 0) + 1

    for letra in palabra2:
        contador_palabra2[letra] = contador_palabra2.get(letra, 0) + 1

    # Verificar si las frecuencias son iguales
    return contador_palabra1 == contador_palabra2

def main():
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    if es_anagrama(palabra1, palabra2):
        print("¡Las palabras son anagramas!")
    else:
        print("Las palabras no son anagramas.")

if __name__ == "__main__":
    main()
