const { DataTypes } = require('sequelize');

const lista_deseos_model = (conexion) => {
    return conexion.define('listaDeseos',{
        listaDeseoId: {
            primaryKey: true,
            type: DataTypes.INTEGER,
            autoIncrement: true,
            field: 'lista_deseo_id'
        }
    },{
        tableName: 't_lista_deseos',
        timestamps: false
    })
}

module.exports = lista_deseos_model;