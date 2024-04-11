def diferencias_entre_cadenas(str1, str2):
    # Convertir las cadenas en conjuntos para obtener caracteres únicos
    set_str1 = set(str1)
    set_str2 = set(str2)

    # Obtener los caracteres presentes en str1 pero no en str2
    out1 = ''.join(caracter for caracter in set_str1 if caracter not in set_str2)

    # Obtener los caracteres presentes en str2 pero no en str1
    out2 = ''.join(caracter for caracter in set_str2 if caracter not in set_str1)

    return out1, out2

# Ejemplo de uso
str1 = "hola"
str2 = "adios"
resultado1, resultado2 = diferencias_entre_cadenas(str1, str2)
print("out1:", resultado1)
print("out2:", resultado2)
