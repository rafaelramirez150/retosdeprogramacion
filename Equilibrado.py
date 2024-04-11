def esta_equilibrado(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    for char in expresion:
        if char in '({[':
            pila.append(char)
        elif char in ')}]':
            if not pila or pila[-1] != pares[char]:
                return False
            pila.pop()
    return not pila

# Ejemplos de uso
expresion_balanceada = "{[a * (c + d)] - 5}"
expresion_no_balanceada = "{a * (c + d)] - 5}"

print("Expresión balanceada:", esta_equilibrado(expresion_balanceada))
print("Expresión no balanceada:", esta_equilibrado(expresion_no_balanceada))
