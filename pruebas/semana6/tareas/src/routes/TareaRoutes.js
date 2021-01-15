// Se puede utilizar destructuración para importar algo cuando queremos usar una parte de una libreria o archivo
const { Router } = require('express');
const {crearTarea, listarTareas, editarTareaPorId, eliminarTareaPorId} = require('../controllers/TareaController'); // importar crearTarea por destructuracion

const tarea_router = Router();

tarea_router.post('/tarea', crearTarea);
tarea_router.get('/tarea', listarTareas);
tarea_router.put('/tarea/:id_tarea', editarTareaPorId);
tarea_router.delete('/tarea/:id_tarea', eliminarTareaPorId);

module.exports = tarea_router;