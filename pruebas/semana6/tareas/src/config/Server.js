const express = require('express');
const bodyParser = require('body-parser');
const tareasRouter = require('../routes/TareaRoutes');

class Server{
    constructor(){
        this.app = express(); // app es una instancia de mi clase express
        this.puerto = process.env.PORT || 5000; // process.env >> ingresamos a las variables de entorno
        // heroku nos asignara un puerto por mientras usaremos el puerto 5000
        this.configurarBodyParser();
        this.rutas();
    }

    // El body parser es la forma en la cual el frontend nos va a mandar la informacion y yo tengo que definir que tipo de informacion voy a recibir (texto plano, json, xml..), sin esta configuración express no sabra que recibir y habra una mala comunicación entre el front y el back
    configurarBodyParser(){
        this.app.use(bodyParser.json());
    }

    // Aqui definiremos todas nuestras rutas raices de nuestra aplicacion para que cuando sean consultadas si no estan aqui automaticamente express retornara un 404(not found)
    rutas(){
        this.app.get('/', (req, res) => {
            // Toda la lógica de nuestra ruta
            res.status(200).send('La API funciona correctamente');
        });
        this.app.use('',tareasRouter);
    }

    start(){
        // llamamos a app y le decimos que se quede escuchando el puerto, y que si todo esta bien que nos imprima por consola.
        this.app.listen(this.puerto, () => {
            console.log(`LA API  esta corriendo exitosamente en el puerto ${this.puerto}`);
        })
    }

}

// Funciona como un export default en React
module.exports = Server