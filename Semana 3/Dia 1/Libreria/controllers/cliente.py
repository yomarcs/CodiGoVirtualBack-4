from flask_restful import Resource, reqparse
from models.cliente import ClienteModel

class ClientesController(Resource):
    def get(self):
        respuesta = ClienteModel.query.all()
        resultado = []
        for cliente in respuesta:
            resultado.append(cliente.devolverClientePrestamo())
        return {
            'ok':True,
            'content':resultado,
            'message': None
        }
    def post(self):
        parseador = reqparse.RequestParser()
        parseador.add_argument(
            'dni',
            required=True,
            type=str,
            help='Falta el dni',
            location='json'
        )
        parseador.add_argument(
            'nombre',
            required=True,
            type=str,
            help='Falta el nombre',
            location='json'
        )
        parseador.add_argument(
            'apellido',
            required=True,
            type=str,
            help='Falta el apellido',
            location='json'
        )
        respuesta = parseador.parse_args()
        cliente = ClienteModel(respuesta['dni'], respuesta['nombre'], respuesta['apellido'])
        cliente.save()
        return {
            'ok': True,
            'message': 'Cliente creado exitosamente',
            'content': cliente.devolverJson()
        }, 201