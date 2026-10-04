# 1. Solicitar datos al usuario
nombre = str(input("Ingrese su nombre: "))
edad_anios = int(input("Ingrese su edad en años: "))
meses_extra = int(input("¿Cuántos meses han pasado desde su último cumpleaños? (0 a 11): "))

# 2. Operaciones aritméticas
# Aproximación considerando años comunes (365 días), días bisiestos (~0.25 días/año) y meses (~30.4 días)
dias_por_anios = edad_anios * 365.25
dias_por_meses = meses_extra * 30.4
total_dias = dias_por_anios + dias_por_meses

# Convierte el total a un número entero para mostrar días completos
total_dias_enteros = int(total_dias)

# 3. Mostrar resultados con print() y f-strings
print("\n" + "="*40)
print("       CÁLCULO DE EDAD EN DÍAS       ")
print("="*40)
print(f"Hola, {nombre} 👋")
print(f"Edad registrada:  {edad_anios} años y {meses_extra} meses")
print(f"Has vivido aprox: {total_dias_enteros:,} días")
print("="*40)