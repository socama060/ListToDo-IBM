document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('agregar-tarea').addEventListener('click', function() {
        var descripcion = document.getElementById('descripcion').value;
        agregarTarea(descripcion);
    });

    document.getElementById('actualizar-tareas').addEventListener('click', function() {
        mostrarTareas();
    });

    function agregarTarea(descripcion) {
        $.ajax({
            type: 'POST',
            url: '/agregar_tarea',
            data: {descripcion: descripcion},
            success: function(response) {
                console.log(response);
                mostrarTareas();
            },
            error: function(error) {
                console.error('Error al agregar la tarea:', error);
            }
        });
    }

    function mostrarTareas() {
        $.ajax({
            type: 'GET',
            url: '/mostrar_tareas',
            success: function(response) {
                $('#tareas').html(response);
            },
            error: function(error) {
                console.error('Error al obtener las tareas:', error);
            }
        });
    }

    mostrarTareas();
});
