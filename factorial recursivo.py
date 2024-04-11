def factorial_recursivo(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial de (n-1)
    else:
        return n * factorial_recursivo(n - 1)

# Ejemplo de uso
numero = 5
factorial = factorial_recursivo(numero)
print(f"El factorial de {numero} es: {factorial}")
