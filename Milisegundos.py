def calcular_milisegundos(dias, horas, minutos, segundos):
    # Calcular el total de milisegundos
    total_milisegundos = ((dias * 24 + horas) * 60 + minutos) * 60 + segundos) * 1000
    return total_milisegundos

# Ejemplo de uso
dias = 2
horas = 12
minutos = 30
segundos = 45

milisegundos_totales = calcular_milisegundos(dias, horas, minutos, segundos)
print("Total de milisegundos:", milisegundos_totales)
