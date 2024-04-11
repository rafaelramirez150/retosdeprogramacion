def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def imprimir_primos_rango(rango):
    """Imprime todos los números primos dentro de un rango dado."""
    print(f"Números primos entre 1 y {rango}:")
    for numero in range(2, rango + 1):
        if es_primo(numero):
            print(numero, end=" ")

def main():
    imprimir_primos_rango(100)

if __name__ == "__main__":
    main()
