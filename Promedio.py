# Entrada: Solicitamos la calificación al usuario y la convertimos a float
calificacion = float(input("Ingresa tu calificación (0-100): "))

# Clasificación mediante la estructura if-elif-else
if calificacion >= 90:
    clasificacion = "Excelente"
elif calificacion >= 80:
    clasificacion = "Notable"
elif calificacion >= 70:
    clasificacion = "Bueno"
else:
    clasificacion = "Reprobado"

# Salida: Mostramos el resultado utilizando f-string
print(f"Tu calificación de {calificacion} es: {clasificacion}")