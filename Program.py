class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            print(f"Tarea '{tarea.descripcion}' marcada como completada.")
        except IndexError:
            print("La posición especificada no existe.")

    def mostrar_tareas(self):
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"{i + 1}. {tarea.descripcion} - {estado}")
        else:
            print("No hay tareas pendientes.")

    def eliminar_tarea(self, posicion):
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("La posición especificada no existe.")


def main():
    gestor = GestorTareas()

    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

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
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

# Nueva ruta para guardar los datos online

from flask import Flask, request, jsonify

app = Flask(__name__)

class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        return tarea

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            return f"Tarea '{tarea.descripcion}' marcada como completada."
        except IndexError:
            return "La posición especificada no existe."

    def mostrar_tareas(self):
        if self.tareas:
            tareas_info = []
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                tarea_info = f"{i + 1}. {tarea.descripcion} - {estado}"
                tareas_info.append(tarea_info)
            return tareas_info
        else:
            return ["No hay tareas pendientes."]

    def eliminar_tarea(self, posicion):
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            return f"Tarea '{tarea_eliminada.descripcion}' eliminada."
        except IndexError:
            return "La posición especificada no existe."

gestor = GestorTareas()

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    data = request.get_json()
    descripcion = data.get('descripcion')
    if descripcion:
        tarea = gestor.agregar_tarea(descripcion)
        return jsonify({'mensaje': f'Tarea "{tarea.descripcion}" agregada correctamente'})
    else:
        return jsonify({'error': 'La descripción de la tarea es requerida'})

if __name__ == '__main__':
    app.run(debug=True)
