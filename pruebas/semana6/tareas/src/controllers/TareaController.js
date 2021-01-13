// Aqui se va a definir todos los controladores (comportamiento que va a recibir cuando se llama a una ruta determinada con su método de acceso(GET,POST,PUT,DELETE))
let tareas = [];

const crearTarea = (req, res) => {
    let tarea = req.body;
    // La forma de capturar lo que me manda el usuario mediante el body es por su request (req)
    console.log(tarea);
    tareas.push(tarea);
    return res.json({
        ok: true,
        message: 'Se creo la tarea exitosamente',
        content: tareas
    })
}

const listarTareas = (req, res) => {
    return res.json({
        ok: true,
        message: null,
        content: tareas
    })
}

const editarTareaPorId = (req, res) => {
    // Para capturar un valor pasado por la url se usa el metodo params que nos retorna un diccionario de todas las variables declaradas en el ruta
    let { id_tarea } = req.params;
    // validar que la posición mandada exista, si existe hace el cambio de la tarea y sino, indicar que la tarea no existe
    if(tareas.length > id_tarea){
        // Significa que si existe id
        return res.json({
            ok: true,
            message: 'Se actualizo correctamente la tarea',
            content: id_tarea
        })
    }else{
        // Significa que no existe id
        return res.json({
            ok: false,
            message: `no existe tarea con id ${id_tarea}`,
            content: null
        })
    }
    
}

module.exports = {
    //  Gracias a ES6 se interpreta como crearTarea: crearTarea, es decir que la llave json es igual al nombre de la variable a exportar
    crearTarea,
    listarTareas,
    editarTareaPorId
}


