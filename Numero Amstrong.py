def es_numero_armstrong(numero):
    # Convertir el número en una cadena para contar los dígitos
    num_str = str(numero)
    # Calcular el número total de dígitos
    num_digitos = len(num_str)
    # Calcular la suma de los dígitos elevados al número total de dígitos
    suma = sum(int(digito) ** num_digitos for digito in num_str)
    # Verificar si la suma es igual al número original
    return suma == numero

# Ejemplo de uso
numero = 153
if es_numero_armstrong(numero):
    print(numero, "es un número de Armstrong")
else:
    print(numero, "no es un número de Armstrong")
