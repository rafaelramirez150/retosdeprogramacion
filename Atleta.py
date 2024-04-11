def evaluar_carrera(atleta, pista):
    # Verificar que los parámetros sean válidos
    if not all(x in ['run', 'jump'] for x in atleta):
        print("Error: El array del atleta solo puede contener 'run' o 'jump'")
        return False
    if not all(x in ['_', '|'] for x in pista):
        print("Error: La pista solo puede contener '_' (suelo) o '|' (valla)")
        return False
    
    # Iterar sobre el atleta y la pista simultáneamente
    for accion, obstaculo in zip(atleta, pista):
        # Si el atleta corre en suelo y no hay valla, o salta sobre una valla, todo está bien
        if (accion == 'run' and obstaculo == '_') or (accion == 'jump' and obstaculo == '|'):
            continue
        # Si el atleta salta sobre suelo, cambiamos el suelo a "x"
        elif accion == 'jump' and obstaculo == '_':
            print("Ha saltado sobre el suelo.")
            return False
        # Si el atleta corre sobre una valla, cambiamos la valla a "/"
        elif accion == 'run' and obstaculo == '|':
            print("Ha intentado correr sobre una valla.")
            return False

    # Si el atleta ha recorrido toda la pista sin errores, ha superado la carrera
    print("¡El atleta ha superado la carrera!")
    return True

# Ejemplo de uso
atleta = ['run', 'jump', 'run', 'jump']
pista = '_|_|_|_'

evaluar_carrera(atleta, pista)
