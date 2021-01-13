from flask import Flask, request
app = Flask(__name__)
supermercados = []

@app.route('/')
def inicio():
    return 'El servidor se ha levantado exitosamente'

# methods >> Agregamos los verbos que admite o soporta la ruta
# request >> Esta importacion de la libreria flask nos permitira saber que método se esta utilizando
#            en cada peticion al poder imprimirla en consola >> print(request.method)
@app.route('/supermercado',methods=['GET','POST'])
def ingresar_supermercado():
    print(request.method)
    if request.method == 'GET':
        return {
            'ok': True,
            'content': supermercados,
            'message': None            
        }
    elif request.method == 'POST':
        # request.get_json() >> convierte lo que me llega por el body a un diccionario en python
        print(request.get_json())
        print(request.get_json()['nombreSuper'])
        informacion = request.get_json()
        supermercados.append(informacion)
        return {
            'ok':True,
            'content': supermercados,
            'message': "Se agrego exitosamente el supermercado"
        },201

# Lo único que determina la finalización de un parametro y el inicio de otro es '/'
@app.route('/supermercado/<int:id_super>', methods=['GET','PUT','DELETE'])
def supermercadoPorId(id_super):
# Como verifico que el id que me mande existe en mi lista
#  >> verificamos longitud de lista y comparamos con id
    if len(supermercados) > id_super:
    # El supermercado con el id id_super si existe
        if request.method == 'GET':
            return {
                'ok':True,
                'content': supermercados[id_super],
                'message': None
            }
        elif request.method == 'PUT':
            # request.get_json() >> convierte lo que me llega por el body a un diccionario en python
            data = request.get_json()
            supermercados[id_super] = data
            return {
                'ok': True,
                'content': supermercados[id_super],
                'message': 'Se actualizo el supermercado exitosamente'
            },201
        elif request.method == 'DELETE':
            del supermercados[id_super]
            return {
                'ok': True,
                'content': None,
                'message': 'Se elimino exitosamente el supermercado'
            },204
    # El supermercado con el id id_super No existe
    else:
        return {
            'ok': False,
            'content': None,
            'message': 'El supermercado con la posicion {} no existe'.format(id_super)
        }

if __name__=='__main__':
    app.run(debug=True,port=5001)
