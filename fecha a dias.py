from datetime import datetime

def diferencia_en_dias(fecha1, fecha2):
    try:
        # Convertir las cadenas de texto a objetos datetime
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")
        
        # Calcular la diferencia absoluta en días
        diferencia = abs((fecha2_obj - fecha1_obj).days)
        
        return diferencia
    
    except ValueError as e:
        raise ValueError("Una de las fechas no tiene el formato correcto (dd/MM/yyyy).") from e

# Ejemplo de uso
fecha1 = "10/03/2024"
fecha2 = "15/03/2024"
diferencia = diferencia_en_dias(fecha1, fecha2)
print("Diferencia en días:", diferencia)
