# LISTAS
# En JavaScript se le dice array
colores = ['rojo', 'blanco', 'Azul', 'Violeta']
print(colores)
# Imprime la ultima posicion de la lista
print(colores[-1])
# Imprimir desde la 0 hasta <2
print(colores[0:2])
# Imprimri desde la 1 hasta el final
print(colores[1:])
# LA forma de copiar el contenido ( y ya no estan alojados en la misma posicion de memoria)
colores2 = colores[:]
# colores[0]='verde'
# print(colores2)
# print(colores)

# Todas las formas de impresion de las LISTAS sriben para los textos
nombre = 'Yomar'
# print(nombre[3])

# Metodo para aagregar un nuevo valor dentro de la lista
colores.append('negro')

# Metodos para quitar un valor de la lista
colores.remove('blanco')

# PAra el metodo pop(indice) saca el elemento de la lisra segun su posicion y nos da
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
# coleccion de elemento ordenadas QUE NO SE PUEDE MODEIFICAR
# e inalterable y sirve oara usar eleementis qye nunca se van a modicficar
nombres = ('Yomar', 'Kevin', 'Gabriel', 'Fabian')
# nombres[1] = 'Karen'

# Longitud de una tupla
print(len(nombres))

# Ver si ahy elementos repetidos en una tupla
print(nombres.count('Yomar'))

# ====================================================================== #
# CONJUNTOS
# Coleccion de elementos desordenada, osea que no tiene indice para acceder a sus elementos
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
variable = """
Esto es un texto
Que respeta los saltos de linea
y se usa mayormente para documentacion
"""
print(persona['id'])
persona.pop('id')
del persona['nombre']
persona['apellido'] = 'Cerdán'
print(persona['hobbies']['dificultad'])
print(persona)
print(variable)
