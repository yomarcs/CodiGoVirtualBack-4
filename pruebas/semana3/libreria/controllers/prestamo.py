from flask_restful import Resource, reqparse
from models.prestamo import PrestamoModel
from models.cliente import ClienteModel
from datetime import datetime

class PrestamosController(Resource):
    def get(self):
        resultado = PrestamoModel.query.all()
        respuesta = []
        for prestamo in resultado:
            respuesta.append(prestamo.devolverJson())
            print(prestamo.clientePrestamo.devolverJson())
        return {
            'ok': True,
            'message': None,
            'content': respuesta
        }

    def post(self):
        parseador = reqparse.RequestParser()
        parseador.add_argument(
            'fecha_inicio',
            required=True,
            type=str,
            location='json',
            help='Falta fecha inicio'
        )
        parseador.add_argument(
            'fecha_fin',
            required=True,
            type=str,
            location='json',
            help='Falta fecha fin'
        )
        parseador.add_argument(
            'cliente',
            required=True,
            type=str,
            location='json',
            help='Falta cliente'
        )
        parseador.add_argument(
            'libro',
            required=True,
            type=str,
            location='json',
            help='Falta libro'
        )
        resultado = parseador.parse_args()
        # Al momento de ingresar un nuevo prestamo
        # usar
        # from datetime import datetime
        # datetime.date(datetime.now()) esto lo comparan con la fecha de entregade mi usuario
        # datetime.now
        # 1. Que verifique que el usuario no tenga ningun libro pendiente de devolucion
        # 2. Vea si existen ejemplares de ese libro a prestar(o sea que los prestamos actuales de ese libro no superen la cantidad)
        # 3. Que al momento de realizr el prestamo el libro y el cliente esten con estado true.
        fechaActual = datetime.date(datetime.now())
        # SELECT * FROM T_PRESTAMO WHERE CLI_ID = RESULTADO['CLIENTE]
        prestamoCliente = PrestamoModel.query.filter_by(cliente=resultado['cliente']).all()
        print(prestamoCliente)
        restriccion = 0 # Es una bandera(flag)
        if prestamoCliente:
            # La persona tiene un historial de prestamos
            for prestamo in prestamoCliente:
                print(prestamo.fechentrega_prestamo)
                # La fecha de entrega es la fecha en la cual el cliente va a devolver el libro( aun no estamos ocntrolando las penalidades que pudiese haber) y si hay fecha de entrega significa que el cliente ya devolvio el libro 
                if prestamo.fechentrega_prestamo:
                # if prestamo.fechfin_prestamo > fechaActual:
                    # La fecha de devolucion es mayor que el dia actual por ende hay un prestamo que aun no se devuelve el libro
                    restriccion += 1 # restricion = restriccion + 1
        else:
            # La persona nunca ha realizado un prestamo
            pass
        # prestamo = PrestamoModel(resultado['fecha_inicio'], resultado['fecha_fin'], resultado['cliente'], resultado['libro'])
        # prestamo.save()
        return {
            'ok':True,
            # 'content':prestamo.devolverJson(),
            'message':'Prestamo creado exitosamente'
        },201