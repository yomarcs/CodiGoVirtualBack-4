// Aqui se va a definir todos los controladores (comportamiento que va a recibir cuando se llama a una ruta determinada con su método de acceso(GET,POST,PUT,DELETE))
// array.splice(indice desde donde comenzarar a cambiar el array, numero de elementos a eliminar, elementos que se agregaran sino se especifica elementos splice() solo eliminara elementos del array)

let tareas = [];

const crearTarea = (req, res) => {
    let tarea = req.body;  
    // console.log(req.body); 
    // La forma de capturar lo que me manda el usuario mediante el body es por su request (req)
    console.log(tarea);
    tareas.push(tarea);
    return res.json({
        ok: true,
        message: 'Se creo la tarea exitosamente',
        content: tarea
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
    // console.log(id_tarea);
    // validar que la posición mandada exista, si existe hace el cambio de la tarea y sino, indicar que la tarea no existe
    if(tareas.length > id_tarea-1){
        // Significa que si existe id
        // tarea = req.body;
        // tareas.splice(id_tarea-1,1, tarea);
        tareas[id_tarea-1] = req.body;
        return res.json({
            ok: true,
            message: 'Se actualizo correctamente la tarea',
            content: tareas[id_tarea-1]
        })
    }else{
        // Significa que el id esta fuera de la lonfitud de mis tareas
        return res.json({
            ok: false,
            message: `no existe tarea con id ${id_tarea}`,
            content: null
        })
    }
}

// Eliminar Tarea segun su id
const eliminarTareaPorId = (req, res) => {
    let { id_tarea } = req.params;
    if(tareas.length > id_tarea-1){
        // https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Array/splice
        // array.splice(indice desde donde comenzarar a cambiar el array, numero de elementos a eliminar, elementos que se agregaran sino se especifica elementos splice() solo eliminara elementos del array)
        tareas.splice(id_tarea-1,1); 
        return res.json({
            ok: true,
            content: null,
            message: 'Se elimino tarea correctamente'
        })
    }else {
        return res.status(404).json({
            ok: false,
            message: `No existe tarea con id: ${id_tarea-1}`
        })
    }
}

const devolverTareaPorId = (req, res) => {
    // req.query >> Forma dinamica de recibir parametros sin necesidad de declararla en la ruta 
    //           >> 127.0.0.1:5000/tarea?id=1&parametro2=valor2&parametro3=valor3
    // Validar si en los parametros esta el parametro id y si esta buscarlo en el array y sino esta el id indicar que falta ese parametro con un estado 500 y si no existe  esa posicion indicar que no existe con un estado 404
    let {id} = req.query;
    console.log(req.query.id);
    if(id){
        if(tareas.length > id-1 && id >=1 ){
            return res.status(200).json({
                ok: true,
                message: null,
                content: tareas[id-1]
            })
        }else{
            return res.status(404).json({
                ok: false,
                message: `No existe tarea con id ${id}`,
                content: null
            })
        }
    }else{
        return res.status(500).json({
            ok: false,
            message: `Ocurrio un error al buscar la tarea`,
            content: null
        })
    }

}

module.exports = {
    //  Gracias a ES6 se interpreta como crearTarea: crearTarea, es decir que la llave json es igual al nombre de la variable a exportar
    crearTarea,
    listarTareas,
    editarTareaPorId,
    eliminarTareaPorId,
    devolverTareaPorId
}


