# Colecciones de datos en Python
# Listas [], Tuplas (), Conjuntos {} y Diccionarios

# LISTAS
# En JavaScript se le dice array
#             0        1        2        3
#            -4       -3       -2       -1
colores = ['rojo', 'blanco', 'Azul', 'Violeta']

print(colores)
# Imprime la ultima posicion de la lista
print(colores[-1])
# Imprime desde la pos[0] hasta <2
print(colores[0:2])
# Imprim desde la pos[1] hasta el final
print(colores[1:])
# La forma de copiar el contenido (y ya no estan alojados en la misma posición de memoria)
colores2 = colores[:]
# colores[0]='verde'
# print(colores2)
# print(colores)

# Todas las formas de impresión de las LISTAS sirven para los textos
# El texto es tratado como una lista y podemos imprimir sus posiciones mas no editarlas
nombre = 'Yomar'
# print(nombre[3]) # Imprimira la posición 3  de nombre >> a

# Metodo para aagregar un nuevo valor dentro de la lista
colores.append('negro')

# Metodos para quitar un valor de la lista
colores.remove('blanco')

# Para el método pop(indice) saca el elemento de la lista según su posición y nos da
# la opcion de almacenarlo en un variable
color_eliminado = colores.pop(2)
print(color_eliminado)
print(colores)
del colores[1]
print(colores)

# Metedo para resetear toda la lista y dejarla en blanco
colores.clear()
print(colores)

# ====================================================================== #
# TUPLAS
# colección de elementos ordenados que "NO SE PUEDEN MODIFICAR o ALTERAR"
# Funcionan como variables constantes que podemos usar
# conexiones al servidor, credenciales, metodos de clase, etc
# Las tuplas se representan en paréntesis ()
nombres = ('Yomar', 'Kevin', 'Gabriel', 'Fabian','Yomar')

# Cuando definimos 1 elemento, por buenas prácticas se recomienda poner una 
# coma al final, sino lo hacemos podremos tener problemas con librerias de
# flask y django, pq no la reonocera, pensara que es una llamada a una función.
url = ("192.168.1.1",) 
# nombres[1] = 'Karen' # No soporta asignación, no podemos agregar elementos.

# Longitud de una tupla
print(len(nombres))

# Imprimir un elemento de una tupla
# para definir su posición si funciona igual que las listas , en []
print(nombres[0]) 

# Ver si hay elementos repetidos en una tupla
# Cuántos veces hay Yomar en esta tupla >> 1 vez
print(nombres.count('Yomar')) # >> 2

# ====================================================================== #
# CONJUNTOS
# Coleccion de elementos desordenada, osea que no tiene indice para acceder a sus elementos
# No se utiliza mucho en Desarrollo Web
estaciones = {'Verano', 'Otoño', 'Invierno', 'Primavera'}
print(estaciones)
# La forma de iterar es mediante un FOR 
estaciones.add('OtoñoVerano')
print(estaciones)

# ======================================================================= #
# DICCIONARIOS
# Coleccion d elementos que estan indexados, no estan ordenados por una 
# posicion en concreto sino que manejan una llave y un valor
persona = {
    'id':1,
    'nombre':'Yomar',
    'fecnac':'12/10/84',
    'relacion':'soltero',
    'hobbies':{
        'nombre':'Futbol',
        'dificultad':'Basico'
    }
}
print(persona['id'])
persona.pop('id')
del persona['nombre']
persona['apellido'] = 'Cerdán'
print(persona['hobbies']['dificultad'])
print(persona)

variable = """
Esto es un texto 
Que respeta los saltos de linea
y se usa mayormente para documentacion
"""
print(variable)