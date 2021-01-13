# pip3 install nombre_paquete
# pip3 list (lista todas las librerias instaladas en nuestra maquina)
# pip3 freeze ( nos indic las librerias pero de una manera tecnica
#               usadap para el deploy)

# Importa toda la libreria y puedo usar toda su funcionalidad
import camelcase

# Seleccioneo que clase, funcion, etc voy a utilizar de esa libreria
# from camelcase import Camelcase

# Igual que la forma anterior pero le puedo dar un alias a esa clase,
# función, etc para que se mas facil de usar
# from camelcase import Camelcase as camello

camello = camelcase.CamelCase()  
texto = "Hola Yomar, feliz miercoles"
print(camello.hump(texto))
