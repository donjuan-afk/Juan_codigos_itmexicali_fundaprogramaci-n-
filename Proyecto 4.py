class Equipo:
    """Clase simple para agrupar los datos relacionados de cada equipo."""
    def __init__(self, nombre, ganados, perdidos, empates):
        self.nombre = nombre
        self.ganados = int(ganados)
        self.perdidos = int(perdidos)
        self.empates = int(empates)
        self.puntos = self.calcular_puntos()

    def calcular_puntos(self):
        # Regla del torneo: Ganado = 3 pts, Empate = 1 pt, Perdido = 0 pts
        return (self.ganados * 3) + (self.empates * 1)


def main():
    print("=" * 60)
    print(f"{'SISTEMA DE CONTROL DE TORNEO DEPORTIVO':^60}")
    print("=" * 60)
    
    # 1. Uso de listas y solicitud de datos con input()
    matriz_datos = []
    
    try:
        total_equipos = int(input("\n¿Cuántos equipos desea registrar en el torneo?: "))
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
        return

    print("\n--- INGRESO DE DATOS DE LOS EQUIPOS ---")
    for i in range(total_equipos):
        print(f"\nEquipo #{i + 1}")
        nombre = input("  Nombre del equipo: ")
        ganados = input("  Partidos ganados: ")
        perdidos = input("  Partidos perdidos: ")
        empates = input("  Partidos empatados: ")
        
        # 2. Uso de una matriz (lista de listas) para almacenar la colección de datos en crudo
        fila_equipo = [nombre, ganados, perdidos, empates]
        matriz_datos.append(fila_equipo)

    # 3. Procesamiento utilizando objetos de la clase Equipo
    lista_objetos_equipos = []
    for fila in matriz_datos:
        # Extraemos los datos de la matriz y creamos la instancia de la clase
        eq = Equipo(nombre=fila[0], ganados=fila[1], perdidos=fila[2], empates=fila[3])
        lista_objetos_equipos.append(eq)

    # Ordenar los equipos de mayor a menor según sus puntos
    lista_objetos_equipos.sort(key=lambda x: x.puntos, reverse=True)

    # 4. Mostrar resultados formateados con print() y f-strings
    print("\n\n" + "=" * 60)
    print(f"{'TABLA GENERAL DE POSICIONES':^60}")
    print("=" * 60)
    print(f"{'POS':<5} | {'EQUIPO':<20} | {'G':<3} | {'P':<3} | {'E':<3} | {'PTS':<5}")
    print("-" * 60)

    for indice, eq in enumerate(lista_objetos_equipos, start=1):
        print(f"{indice:<5} | {eq.nombre:<20} | {eq.ganados:<3} | {eq.perdidos:<3} | {eq.empates:<3} | {eq.puntos:<5}")

    print("=" * 60)

    # Identificar al líder del torneo (el que está en la primera posición tras ordenar)
    lider = lista_objetos_equipos[0]
    print(f"\n LÍDER DEL TORNEO: {lider.nombre} (Con {lider.puntos} puntos acumulados)\n")


# Ejecutar el programa principal
if __name__ == "__main__":
    main() 