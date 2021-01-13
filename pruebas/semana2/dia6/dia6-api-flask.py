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
        return 'Me hiciste un GET'
    elif request.method == 'POST':
        return 'Me hiciste un POST'
   #return 'Se registro el supermercado'
# GET >> Se usa para solicitar información
# POST >> Se usa para crear nueva información
# PUT >> Se usa para actualizar algún registro
# DELETE >> Se usa para eliminar algún registro
# Sino declaramos métodos(verbos), por defecto el unico método permitido va a ser el GET

if __name__=='__main__':
    app.run(debug=True,port=5001)