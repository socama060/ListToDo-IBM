document.addEventListener('DOMContentLoaded', function() {
    // Agregar evento de envío de formulario para agregar tarea
    document.getElementById('form-agregar').addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar que se envíe el formulario automáticamente
        
        var descripcion = document.getElementById('descripcion').value;
        
        // Enviar los datos al servidor Python
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/agregar_tarea'); // Ruta relativa para agregar una tarea
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log('Tarea agregada exitosamente');
                mostrarTareas(); // Actualizar la lista de tareas después de agregar una nueva tarea
            } else {
                console.error('Error al agregar la tarea:', xhr.statusText);
            }
        };
        xhr.send(JSON.stringify({ descripcion: descripcion }));
    });
    
    // Función para mostrar las tareas
    function mostrarTareas() {
        var listaTareas = document.getElementById('tareas');
        
        // Limpiar la lista de tareas existente
        listaTareas.innerHTML = '';
        
        // Obtener las tareas del servidor Python
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/mostrar_tareas');
        xhr.onload = function() {
            if (xhr.status === 200) {
                var tareas = JSON.parse(xhr.responseText);
                tareas.forEach(function(tarea, index) {
                    // Crear un nuevo elemento de lista para cada tarea
                    var elementoTarea = document.createElement('li');
                    elementoTarea.textContent = `${index + 1}. ${tarea.descripcion} - ${tarea.completada ? 'Completada' : 'Pendiente'}`;
                    elementoTarea.classList.add('tarea');
                    if (tarea.completada) {
                        elementoTarea.classList.add('completed');
                    }
                    listaTareas.appendChild(elementoTarea);
                });
            } else {
                console.error('Error al obtener las tareas:', xhr.statusText);
            }
        };
        xhr.send();
    }
    
    // Mostrar las tareas al cargar la página
    mostrarTareas();
});
