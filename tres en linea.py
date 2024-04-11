def analizar_matriz(matriz):
    # Verificar proporción de "X" y "O"
    num_x = sum(fila.count("X") for fila in matriz)
    num_o = sum(fila.count("O") for fila in matriz)
    num_vacios = sum(fila.count("") for fila in matriz)
    
    if num_x != num_o and num_x != num_o + 1:
        return "Nulo"

    # Verificar si algún jugador ha ganado
    for i in range(3):
        # Filas
        if matriz[i][0] == matriz[i][1] == matriz[i][2] and matriz[i][0] != "":
            return matriz[i][0]
        # Columnas
        if matriz[0][i] == matriz[1][i] == matriz[2][i] and matriz[0][i] != "":
            return matriz[0][i]
    # Diagonales
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != "":
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != "":
        return matriz[0][2]

    # Verificar empate
    if num_vacios == 0:
        return "Empate"

    return "Nulo"

# Ejemplo de uso
matriz_juego = [
    ["X", "X", "X"],
    ["X", "O", "O"],
    ["O", "O", ""]
]

resultado = analizar_matriz(matriz_juego)
print("Resultado:", resultado)
