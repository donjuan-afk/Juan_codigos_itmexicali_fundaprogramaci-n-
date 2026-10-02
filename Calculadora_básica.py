#Programa: Calculadora básica con manejo de errores

#1. Pide dos números al usuario usando float(int(input())
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

#2. Calcula la suma, resta y multiplicación 
suma = num1 + num2 
resta = num1 - num2
multiplicacion = num1 * num2 

#3. Muestra los resultados usando f-strings 
print("\n--- Resultados de las Operaciones ---")
print(f"Suma ({num1} + {num2}): {suma}")
print(f"Resta ({num1} - {num2}): {resta}")
print(f"Multiplicación ({num1} * {num2}): {multiplicacion}")

#Manejo de la división entre cero usando if-else
if num2 == 0:
    print("División: Error: División entre cero")
else:
    division = num1/num2 
    print(f"División ({num1} / {num2}): {division}") 