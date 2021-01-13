const { DataTypes } = require('sequelize');

const usuario_model = (conexion) => {
    let usuario =  conexion.define('usuarios',{
        usuarioId: {
            primaryKey :true,
            autoIncrement: true,
            type: DataTypes.INTEGER,
            field: 'usuaio_id'
        },
        usuarioCorreo: {
            // https://sequelize.org/master/manual/validations-and-constraints.html#validators
            type: DataTypes.STRING(40),
            field: 'usuario_correo',
            unique: true,
            allowNull: false,
            validate:{
                len: [10,30],
                isEmail: true,
                isAlphanumeric: true,
            }

        },
        usuarioNombre: {
            type: DataTypes.STRING(45),
            field: 'usuario_nombre',
            unique: true,
            allowNull: false
        },
        usuarioDireccion: {
            type: DataTypes.STRING(255),
            field: 'usuario_direccion',
            allowNull: false
        },
        usuarioTelefono: {
            type: DataTypes.STRING(10),
            unique: true,
            validate: {
                isNumeric: true,
                min: 9000000000,
                max: 9999999999
            }
        },
        usuarioHash: {
            field: 'usuario_hash',
            type: DataTypes.TEXT
        },
        usuarioSalt: {
            field: 'usuario_salt',
            type: DataTypes.TEXT
        },
        usuarioFechaNacimiento: {
            field: 'usuario_fecha_nacimiento',
            type: DataTypes.DATEONLY
        }
    },{
        tableName: 't_usuario',
        timestamps: false
    })

    // creamos y retornamos usuario pq aqui ira la incriptacion de la contraseña
    return usuario;
}

module.exports = usuario_model;