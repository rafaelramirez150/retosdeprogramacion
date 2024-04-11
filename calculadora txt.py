def calcular_resultado():
    resultado = None
    with open("Challenge21.txt", "r") as archivo:
        for linea in archivo:
            try:
                linea = linea.strip()
                if not linea:
                    continue  # Ignorar líneas vacías
                if resultado is None:
                    resultado = float(linea)
                else:
                    operador = linea[0]
                    operando2 = float(linea[1:])
                    resultado = resolver_operacion(resultado, operando2, operador)
            except ValueError as e:
                print("No se han podido resolver las operaciones:", e)
                return
    print("El resultado es:", resultado)

calcular_resultado()
