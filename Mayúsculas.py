def capitalizar_primera_letra(texto):
    # Dividir el texto en palabras utilizando espacios como separador
    palabras = texto.split()
    # Crear una lista vacía para almacenar las palabras capitalizadas
    palabras_capitalizadas = []
    # Iterar sobre cada palabra
    for palabra in palabras:
        # Capitalizar la primera letra de la palabra y concatenar el resto del texto
        palabra_capitalizada = palabra[0].upper() + palabra[1:]
        # Agregar la palabra capitalizada a la lista
        palabras_capitalizadas.append(palabra_capitalizada)
    # Unir las palabras capitalizadas en un solo string separadas por espacios
    texto_capitalizado = ' '.join(palabras_capitalizadas)
    return texto_capitalizado

# Ejemplo de uso
texto_ejemplo = "hola, cómo estás?"
print(capitalizar_primera_letra(texto_ejemplo))  # Devuelve "Hola, Cómo Estás?"
