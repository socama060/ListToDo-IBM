import csv
import os

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True
            print(f"Tarea '{self.tareas[posicion]["descripcion"]}' marcada como completada.")
        except IndexError:
            print("La posición especificada no existe.")

    def mostrar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i + 1}. {tarea["descripcion"]} - {estado}")
        else:
            print("No hay tareas pendientes.")

    def eliminar_tarea(self, posicion):
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada["descripcion"]}' eliminada.")
        except IndexError:
            print("La posición especificada no existe.")

    def guardar_tareas(self):
        ruta_archivo = "C:/Users/sonia/OneDrive/Escritorio/Sonia/Programación/ListToDo/data/tareas.csv"
        with open(ruta_archivo, "w", newline="") as archivo_csv:
            campos = ["descripcion", "completada"]
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(self.tareas)

def main():
    gestor = GestorTareas()

    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Guardar las tareas en archivo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            gestor.mostrar_tareas()
            posicion = int(input("Ingrese la posición de la tarea completada: ")) - 1
            gestor.marcar_completada(posicion)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            gestor.mostrar_tareas()
            posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(posicion)
        elif opcion == "5":
            gestor.guardar_tareas()
            print("Tareas guardadas en el archivo.")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
