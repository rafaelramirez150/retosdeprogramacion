def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    
    return binario

# Ejemplo de uso
numero_decimal = int(input("Ingrese un número decimal: "))
binario_resultante = decimal_a_binario(numero_decimal)
print("El número decimal", numero_decimal, "equivale a", binario_resultante, "en binario.")
