# pip3 install flask-restful
# flask_restful >> Esta libreria sirve para determinar todo el comportamiento mediante clases.
#                  (verbos get, post, put, delete) ahora pasaran a ser métodos de una clase.
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
# reqparse >> Validador que sirve para indicar que ciertos valores o caracteristicas deben de
#             cumplirse para continuar la logica de nuestra api
#          >> Podemos utilizarlo afuera o adentro del metodo, pero dentro de la clase
# Api >> Sirve para agregar un recurso a la api y las rutas mediante 
#        las cuales pondemos acceder a esos recursos

app = Flask(__name__)
api = Api(app) 

items=[{
    'prodNom': 'Sapolio',
    'prodPrec':5.40,
    'prodCar':['LIMPIA TODO','DESENGRASANTE','LAVAVAJILLAS']
},{
    'prodNom':'Ayudin',
    'prodPrec':3.8,
    'prodCar':['ESPONJA GRATIS','LIQUIDO','DESENGRASANTE', 'PULIDOR']
},{
    'prodNom':'PEPSI 3L',
    'prodPrec':5.8,
    'prodCar':['GASEOSA','CARBONATADA','LIQUIDO','ALTO EN AZUCAR']
}]

@app.route('/')
def inicio():
  return 'La api funciona'

# DE ACUERDO A UN BUSCADOR QUE ME INDIQUE TODOS LOS PRODUCTOS QUE TENGAN ESA CARACTERISTICA
# 127.0.0.1/buscar {"palabra":"Liquido"}
@app.route('/buscar',methods=['POST'])
def buscar():
    # Usar doble for
    data = request.get_json()
    palabra = data['palabra']
    print(palabra)
    resultado = []
    for item in items:
        print(item['prodCar'])
        # Usando el metodo upper() y lower() filtrar ya se sea si se ingresa la palabra en mayus o en minus
        for caracteristica in item['prodCar']:
            if caracteristica.lower() == palabra.lower():
                resultado.append(item)
            print(caracteristica)
    return {
        'ok': True,
        'content': resultado
    }

class Item(Resource):
    # reqparse >> Validador que sirve para indicar que ciertos valores o caracteristicas 
    #             deben de cumplirse para continuar la logica de nuestra api.
    # reqparse >> Podemos utilizarlo afuera o adentro del metodo, pero dentro de la clase
    # parser >> instancia de RequestParser
    parser = reqparse.RequestParser()
    parser.add_argument(
        # Creamos argumentos que el usuario nos tendra que pasar obligatoriamente
        'prodNom',
        type=str,
        required=True,
        help='Falta el nombre del producto'
    )
    parser.add_argument(
        # Creamos argumentos que el usuario nos tendra que pasar obligatoriamente
        'prodPrec',
        type=float,
        required=True,
        help='Falta el precio del producto'
    )
    parser.add_argument(
        'prodCar',
        type=list,
        required=True,
        location='json',
        help='Falta las caracteristicas del producto'
    )

    def get(self, id): 
        if len(items) > id:
            return {
                'ok': True,
                'message':None,
                'content': items[id]
            }
        else:
            return {
                'ok':False,
                'message': 'No se encontro el item con id {}'.format(id),
                'content': None
            }
    def post(self):
        data = self.parser.parse_args()
        items.append(data)
        return{
            'ok':True,
            'message': 'Se Agrego exitosamente el item',
            'content': data
        }
    def put(self,id):
        if len(items) > id:
            data = self.parser.parse_args()
            items[id] = data
            return {
                'ok': True,
                'message':None,
                'content': data
            }
        else:
            return {
                'ok':False,
                'message': 'No se encontro el item con id {}'.format(id),
                'content': None
            }
    def delete(self,id):
        if len(items) > id:
            items.pop(id)
            return {
                'ok':True,
                'message':'El item fue eliminado exitosamente',
                'content': None
            }
        else:
            return {
                'ok':False,
                'message': 'No se encontro el item con id {}'.format(id),
                'content': None
            }

        

# Con el uso del flask_restful ya no se necesita decoradores,
# solamente se pasa un parametro para agregar un recurso a la api.
# aunque podemos combinarlos y utilizar el decorador para una ruta especifica.
# Api >> Sirve para agregar un recurso(clase) a la api y las rutas mediante 
#        las cuales pondemos acceder a sus recursos internos(get,post,put,delete).
api.add_resource(Item,'/item','/item/<int:id>')

if __name__=='__main__':
    app.run(debug=True)