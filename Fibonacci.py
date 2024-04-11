def fibonacci(n):
    """Genera los primeros n números de la sucesión de Fibonacci."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

def main():
    n = 50
    fib_sequence = fibonacci(n)
    print("Los primeros 50 números de la sucesión de Fibonacci son:")
    print(fib_sequence)

if __name__ == "__main__":
    main()
