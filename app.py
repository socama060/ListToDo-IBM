from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    descripcion = request.form['descripcion']
    guardar_tarea(descripcion)
    return 'Tarea agregada correctamente'

def guardar_tarea(descripcion):
    df = pd.DataFrame({'Descripcion': [descripcion]})
    df.to_excel(r'C:\Users\sonia\OneDrive\Escritorio\Sonia\Programación\ListToDo\data\tareas.xlsx', index=False)

if __name__ == '__main__':
    app.run(debug=True)
