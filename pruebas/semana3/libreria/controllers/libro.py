from flask_restful import Resource, reqparse
from models.libro import LibroModel

class LibrosController(Resource):
    def get(self):
        resultado = (LibroModel.query.all()) # SELECT * FROM T_LIBRO
        respuesta = []
        for libro in resultado:
            respuesta.append(libro.devolverJson())
            print(libro.devolverJson())
        return {
            'ok' : True,
            'content': respuesta, # Solo podemos devolver 3 tipos de parametros: String, Lista, Diccionario
            'message': None # mayormente se utiliza para mensajes de error.
        }
    def post(self):
        # reqparse >> Validador que sirve para indicar que ciertos valores o características 
        #             deben de cumplirse para continuar la lógica de nuestra api.
        # reqparse >> Podemos utilizarlo afuera o adentro del metodo, pero dentro de la clase
        # parseador >> instancia de RequestParser
        parseador = reqparse.RequestParser()
        # Una vez declarada la instancia de la clase RequestParser tenemos que declarar que argumentos van a ser encargados de la validación y todo argumento que no lo declare y me lo pase el FrontEnd va a ser eliminado
        parseador.add_argument(
            'nombre',
            type = str,
            required=True,
            location='json',
            help='Falta el campo nombre'
        )
        parseador.add_argument( 
            'edicion',
            type=str,
            required=True,
            location='json',
            help='Falta el campo edicion'
        )
        parseador.add_argument(
            'autor',
            type=str,
            required=True,
            location='json',
            help='Falta el campo autor'
        )
        parseador.add_argument(
            'cantidad',
            type=int,
            required=True,
            location='json',
            help='Falta el campo cantidad'
        )
        parseador.add_argument(
            'estado',
            type=bool,
            required=False,
            location='json'
        )
        # Gracias al metodo parse.args se va a validar que todo los argumentos se esten pasando de la manera correcta
        resultado = parseador.parse_args()
        # Al momento de ingresar un nuevo prestamo
        # 1. Que verifique que el usuario no tenga algun libro pendiente de devolucion
        # 2. Que ademas vea si existen ejemplares de ese libro a prestar(o sea que los
        #    prestamos actuales de ese libro no superen a la cantidad del mismo)
        # Creo una nueva instancia de mi modelo
        nuevoLibro = LibroModel(resultado['nombre'],resultado['edicion'],resultado['autor'],resultado['cantidad'])
        # guardo los cambios y los almaceno en la base de datos
        nuevoLibro.save()
        # print(nuevoLibro.id_libro)
        return{
            'ok':True,
            'message':'Libro creado con exito',
            'content': nuevoLibro.devolverJson()
        },201
        
class LibroController(Resource):
    def get(self,id):
        # Modificar el metodo get por x id para qu eme devuelva todos los prestamos de ese libro
        # hint:  agregar un metodo en el modelo

        # select * from t_libro where param=valor
        # first() >> Al usar el metdo first nos va  a devolver la primera coincidencia  y ya no una lista, sino un objeto en concreto y sino cumple la condicion retorna None
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        # delvolver en el content todo el libro y si  no hubiece indicar que no se encuentra ese libro con esa peticion con un status 404
        if resultado:
            # si hay un libro
            return{
                'ok': True,
                'content': resultado.devolverLibroPrestamo()
            }
        else:
            # Si no hay libro con ese id
            return {
                'ok': False,
                'content': None,
                'message': 'No existe ese libro'
            },404

    def put(self,id):
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        if resultado:
            parseador = reqparse.RequestParser()
            parseador.add_argument(
            'nombre',
            type = str,
            required=False,
            location='json',
            help='Falta el campo nombre'
            )
            parseador.add_argument(
                'edicion',
                type=str,
                required=False,
                location='json',
                help='Falta el campo edicion'
            )
            parseador.add_argument(
                'autor',
                type=str,
                required=False,
                location='json',
                help='Falta el campo autor'
            )
            parseador.add_argument(
                'cantidad',
                type=int,
                required=False,
                location='json',
                help='Falta el campo cantidad'
            )
            parseador.add_argument(
            'estado',
            type=bool,
            required=False,
            location='json'
            )
            body = parseador.parse_args() # parametro=valor, parametro2=valor2......
            resultado.update(nombre = body['nombre'], edicion = body['edicion'], autor = body['autor'], cantidad = body['cantidad'])
            return {
                'ok': True,
                'content': resultado.devolverJson(),
                'message': 'Libro actualizado con exito'
            }
        else:
            # Si no hay libro con ese id
            return {
                'ok': False,
                'content': None,
                'message': 'No existe ese libro'
            },404

    def delete(self, id):
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        if resultado:
            # No es recomendable utilizar delete o borrar la informacion, pq borramos data importante para los reportes
            # ante esto podemos agregar el campo estado e inhabilitar el atributo para no perder la informacion que contenga
            # resultado.delete()
            resultado.inhabilitarLibro()
            return {
                'ok': True,
                'content':None,
                'message': 'Se inhabilito exitosamente el Libro'
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe ese libro'
            }, 404