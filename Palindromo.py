def es_palindromo(texto):
    # Eliminar espacios, signos de puntuación y convertir a minúsculas
    texto_limpio = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    # Comparar el texto con su reverso
    return texto_limpio == texto_limpio[::-1]

# Ejemplo de uso
texto = "Ana lleva al oso la avellana."
resultado = es_palindromo(texto)
print(resultado)  # Salida: True
