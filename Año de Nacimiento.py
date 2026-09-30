# Pedir el nombre al usuario (cadena de texto)
nombre = input("Ingresa tu nombre: ")

# Pedir el año de nacimiento y convertirlo a entero (int)
anio_nacimiento = int(input("Ingresa el año de tu nacimiento: "))

# Calcular la edad aproximada utilizando la operación aritmética dada
edad = 2026 - anio_nacimiento

# Pedir la estatura y me convertirla a flotante (float)
estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

# Mostrar la información organizada utilizando f-strings
print("\n--- RESUMEN DE DATOS ---")
print(f"Hola, {nombre}.")
print(f"Tienes aproximadamente {edad} años (naciste en {anio_nacimiento}).")
print(f"Tu estatura es de {estatura} metros.") 