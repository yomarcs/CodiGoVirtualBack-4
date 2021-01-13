from flask import Flask
from base_de_datos import bd
from flask_restful import Api
# >> Importamos desde la carpeta models la clase LibroModel del archivo libro 
# from models.libro import LibroModel
# >> Importamos desde la carpeta controllers la clase LibroController del archivo
#    libro, este a su vez ya tiene importado LibroModel por lo que comentamos su 
#    importacion desde la carpeta models para evitar una importacion circular
from controllers.libro import LibrosController, LibroController
# Importamos desde la carpeta models la clase CLienteModel del archivo cliente
# from models.cliente import ClienteModel
from controllers.cliente import ClientesController
# Importamos desde la carpeta models la clase PrestamoModel del archivo prestamo
# from models.prestamo import PrestamoModel
from controllers.prestamo import PrestamosController

# pip3 install mysqlclient >> Al instalar mysqlclient puede que tengamos problemas, puede que aparesca un montón
#                             de letras rojas y eso es pq la ultima version de python no ha sabido bien clasificar
#                             donde se ubican lpos archivos tanto de 32 bits como de 64 bit
# Solución >> tenemos que descrgar una libreria no oficial desde google: unofficial binaries python
#             https://www.lfd.uci.edu/~gohlke/pythonlibs/  estando en la pagina presionamos f3 para buscar mysqlclient
#             descargamos el numero de complilacion mayor, en nuestro caso pc-39 y dependiendo del SO
#             seleccinamos win32.whl(32bit) o win_amd64.whl(64bits)
# Entramos en la carpeta de descarga en la barra de navegación esribimos cmd para abrir la terminal en esa ubicacion
# corremos la siguiente sentencia >> pip3 install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
# Como ayuda al momento de escribir las primeras letras del mysqlclient podemos presionar la tecla tab autocompletar el nombre

# Gracias a esta linea es que podemos levantar el servidor de backend
app=Flask(__name__)

# >> Creamos una instancia de la clase Api en la cual le tenemos que pasar la app para 
#    que pueda registrar posteriormente todas mis rutas con sus respectivos controladores,
#    sino hago esto, todos los controladores registrados no se podran usar.
# Api >> Sirve para agregar un recurso(clase) a la api y las rutas mediante 
#        las cuales pondemos acceder a sus recursos internos(get,post,put,delete).
api = Api(app=app)

# app.config >> este atributo de la instancia app de la clase FLask almacena todos los 
#               variables de configuración tales como: claves jwt, cadenas de configuración
#               a la base de datos, socket, brodcast, etc.
# print(app.config) #se guarda en forma de diccionario
# Cadena de conexión a la base de datos
# app.config[     'LLave'           ]='tipo-bd://usuario:password@servidor/nomb-bd'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:&&YomarCs84&&@localhost/libreriavirtual'
# error 1049 >> Pq debemos crear la base de datos manualmente desde workbench : create database libreriavirtual
# error 2059 >> error del mismo servidor: la bd rechaza la peticion por cuestiones de seguridad
#            >> Por lo que corremos el siguiente script en workbench para dar permiso para que 
#               se puede acceder desde fuera nuestro servidor para cuestiones de las Apis
#            >> # ALTER USER 'usuario'@'servidor' IDENTIFIED WITH mysql_native_password by 'password';
#                 ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by '&&YomarCs84&&';
# select * from mysql.user; >> script para ver todos los usuarios de nuestro mysql en workbench
# Link cons las formas de conectarse a las diferentes base de datos como MariaDB, posgress, MySQL, etc
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format

# sirve para evitar el warning de que la funcionalidad del sqlalchemy de track modification en un futuro estará deprecada
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# @app.before_first_request >> Este decorador hace que lo que primero que se ejecute en nuestra aplicación
# ni bien se levante el servidor sea el metodo creacion_bd, creando asi la base de datos antes que cualquier
# solicitud (get,post,put,delete) que el usuario pueda realizar
@app.before_first_request
def creacion_bd():
    # Inicio la aplicación pasandole la instancia app que internamente va a buscar la llave 
    # 'SQLALCHEMY_DATABASE_URI' y si la encuentra va a conectar con la base de datos
    bd.init_app(app) # inicializamos la base de datos
    
    # Realiza la eliminacion de todos los modelos en mi base de datos
    bd.drop_all(app=app)

    # Realiza la creación de todos los modelos(tablas) de la base de datos definidos anteriormente
    bd.create_all(app=app)

@app.route('/')
def inicio():
    return 'La API se levanto exitosamente'

# definiendo las rutas de mi aplicación
# en el add_resource van 2 o mas parametros, obligatoriamente en el primero va el recurso
# (comportamiento) y en el segundo van las rutas de acceso
api.add_resource(LibrosController, '/libro')
api.add_resource(LibroController, '/libro/<int:id>')
api.add_resource(ClientesController, '/cliente')
api.add_resource(PrestamosController, '/prestamo')

if __name__ == "__main__":
    app.run(debug=True)

# INSERT INTO `libreriavirtual`.`t_cliente` (`cli_dni`, `cli_nomb`, `cli_ape`, `estado`) VALUES ('42731171', 'Yomar', 'Cerdán S', '1');
# INSERT INTO `libreriavirtual`.`t_cliente` (`cli_dni`, `cli_nomb`, `cli_ape`, `estado`) VALUES ('15481526', 'Gabriel', 'Cerdán DLC', '1');
# INSERT INTO `libreriavirtual`.`t_cliente` (`cli_dni`, `cli_nomb`, `cli_ape`, `estado`) VALUES ('57687902', 'Fabian', 'Cerdán R', '1');
# INSERT INTO `libreriavirtual`.`t_libro` (`lib_nom`, `lib_edicion`, `lib_autor`, `lib_cant`, `estado`) VALUES ('Winnie Pooh', '2020-02-01', 'Condorito', '2', '1');
# INSERT INTO `libreriavirtual`.`t_libro` (`lib_nom`, `lib_edicion`, `lib_autor`, `lib_cant`, `estado`) VALUES ('Star wars', '2020-07-22', 'bryce', '5', '1');
# INSERT INTO `libreriavirtual`.`t_libro` (`lib_nom`, `lib_edicion`, `lib_autor`, `lib_cant`, `estado`) VALUES ('Harry Potter', '2020-04-10', 'llosa', '3', '1');
# INSERT INTO `libreriavirtual`.`t_prestamo` (`prestamo_fechin`, `prestamo_fechfin`, `prestamo_fechentrega`, `estado`, `cli_id`, `lib_id`) VALUES ('2020-12-03', '2020-12-05', '2020-12-05', '1', '1', '1');
# INSERT INTO `libreriavirtual`.`t_prestamo` (`prestamo_fechin`, `prestamo_fechfin`, `prestamo_fechentrega`, `estado`, `cli_id`, `lib_id`) VALUES ('2020-12-06', '2020-12-07', '2020-12-07', '1', '1', '1');
# INSERT INTO `libreriavirtual`.`t_prestamo` (`prestamo_fechin`, `prestamo_fechfin`, `estado`, `cli_id`, `lib_id`) VALUES ('2020-12-07', '2020-12-10', '1', '2', '3');