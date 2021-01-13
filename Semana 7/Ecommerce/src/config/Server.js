const express = require('express');
const bodyParser = require('body-parser');
const { conexion } = require('./Sequelize');
const categoria_router = require('../routes/CategoriaRoutes')

module.exports = class Server{
    constructor(){
        this.app = express();
        this.puerto = process.env.PORT || 5000;
        this.CORS();
        this.configurarBodyParser();
        this.rutas();
    }

    // https://dev.to/lydiahallie/cs-visualized-cors-5b8h   revisar!!
    CORS(){
        this.app.use((req, res, next) => {
            res.header('Access-Control-Allow-Origin','http://localhost:4200');
            res.header('Access-Control-Allow-Headers','Content-Type, Authorization');
            res.header('Access-Control-Allow-Methods','GET,POST,PUT,DELETE');
            next();
        })
    }

    configurarBodyParser(){
        this.app.use(bodyParser.json());
    }

    rutas(){
        this.app.get('/', (req, res) => {
            res.status(200).send('La API funciona correctamente 😎🍕')
        })
        this.app.use('', categoria_router);
    }

    start(){
        this.app.listen(this.puerto, () =>{
            console.log(`Servidor corriendo exitosamente en el puerto ${this.puerto}`);
            // force:true
            conexion.sync().then(()=> {
                console.log('Base de datos sincronizada exitosamente')
            }).catch((error) => {
                console.log(error);
            })
        });
    }
}