import asyncio

async def suma_asincrona(numero1, numero2, segundos):
    # Esperar durante el tiempo especificado
    await asyncio.sleep(segundos)
    # Realizar la suma
    resultado = numero1 + numero2
    return resultado

async def main():
    # Llamar a la función de suma asíncrona
    resultado = await suma_asincrona(10, 20, 3)
    print("El resultado es:", resultado)

# Ejecutar el programa principal
asyncio.run(main())
