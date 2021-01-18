const express = require('express');
const bodyParser = require('body-parser');

module.exports = class Server{
    constructor(){
        this.app = express();
        this.puerto = process.env.PORT || 5000;
        this.configurarBodyParser();
        this.rutas();
    }

    configurarBodyParser(){
        this.app.use(bodyParser.json());
    }

    rutas(){
        this.app.get('/', (req, res) => {
            res.status(200).send('La API funciona correctamente 🍕🍕');
        })
    }

    start(){
        this.app.listen(this.puerto, () => {
            console.log(`El servidor esta corriendo exitosamente en el puerto ${this.puerto}`);
        })
    }

}

