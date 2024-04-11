def invertir_cadena(texto):
    # Convertir la cadena de texto a una lista de caracteres
    caracteres = list(texto)
    
    # Invertir la lista de caracteres
    inicio = 0
    fin = len(caracteres) - 1
    while inicio < fin:
        caracteres[inicio], caracteres[fin] = caracteres[fin], caracteres[inicio]
        inicio += 1
        fin -= 1
    
    # Convertir la lista de caracteres nuevamente a una cadena de texto
    texto_invertido = ''.join(caracteres)
    
    return texto_invertido

# Ejemplo de uso
cadena = "Hola mundo"
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)  # Salida: "odnum aloH"
