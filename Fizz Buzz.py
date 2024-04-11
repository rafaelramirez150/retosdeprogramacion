def fizz_buzz(n):
    """
    Imprime los números del 1 al n, pero para los múltiplos de 3 imprime "Fizz",
    para los múltiplos de 5 imprime "Buzz" y para los múltiplos de ambos 3 y 5
    imprime "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    n = int(input("Ingrese un número para Fizz Buzz: "))
    fizz_buzz(n)

if __name__ == "__main__":
    main()
