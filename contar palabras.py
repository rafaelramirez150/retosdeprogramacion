def contar_palabras(texto):
    # Eliminar signos de puntuación y dividir el texto en palabras
    palabras = texto.split()
    palabras_limpias = [palabra.strip(".,!?;:") for palabra in palabras]

    # Crear un diccionario para contar la frecuencia de cada palabra
    contador = {}
    for palabra in palabras_limpias:
        palabra = palabra.lower()
        contador[palabra] = contador.get(palabra, 0) + 1

    return contador

def imprimir_recuento(recuento):
    print("Recuento de palabras:")
    for palabra, cantidad in recuento.items():
        print(f"{palabra}: {cantidad}")

# Ejemplo de uso
texto = "Hola, hola mundo. Mundo, mundo. Hola!"
recuento = contar_palabras(texto)
imprimir_recuento(recuento)
