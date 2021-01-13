const e = require('express');
const {Categoria} = require('../config/Sequelize');

// Podemos utilizar 2 formas para construir
// 1. create (crear)
// 2. Build(construir), luego save(guardar)

// Creación de categoria
const createCategoria  = async(req,res) => {
    try{
        let nuevaCategoria = await Categoria.create(req.body);
        return res.status(201).json({
            ok: true,
            message: 'Categoria creada exitosamente',
            content: nuevaCategoria
        });
    }catch (error) {
        return res.status(500).json({
            ok: false,
            message: 'Hubo un error al crear la categoria',
            content: error
        });
    }
}

module.exports = {
    createCategoria
}