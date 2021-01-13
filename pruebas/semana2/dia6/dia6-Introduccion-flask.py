# pip3 install flask
# pip3 list

from flask import Flask

# __name__ sirve para definir que nuestra aplicacion de Flask 
# se va a ejecutar en el hilo principal del compilador de python
# print(__name__) >> __main__
app = Flask(__name__)

# siempre para indicar el comportamiento de una ruta tiene que ir en un 
# decorador y luego definir su funcion con todo su comportamiento.
@app.route('/')
def inicio():
    return 'El servidor se ha levantado exitosamente'




# app.run() >> para correr nuestra apliacion, podemos agregarle parametros opcionales como:
# debug=True >> sirve para que cuando hagamos un cambio en nuestra  
#               aplicacion, al momento de guardarse se reinicie el servidor
#            >> Por defecto esta en debug=False
# port=5001 >> El número de puerto por donde se levantara el servidor
#           >> Por defecto es el port=5000 
#           >> Si tengo corriendo mi proyecto de react en el puerto 5000 podemos utilizar otro puerto para levantar el servidor
# la condicional __name__ == __main__ sirve muy parecido al void main(){}, es decir sirve para usar la parte principal del compilador
if __name__ == '__main__':
    app.run(debug=True,port=5001) 


