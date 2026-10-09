# Inicializamos el acumulador en 0.0 para guardar la suma total
suma = 0.0
numero = float(input("Ingresa un número (negativo para terminar): "))

# Iniciamos el bucle 
while True:
    # Si el número es negativo, rompemos el ciclo inmediatamente con break
    if numero < 0:
        break
        
    suma += numero
    numero = float(input("Ingresa otro número (negativo para terminar): "))

# Salida: suma total de los numeros 
print(f"La suma total es: {suma}")