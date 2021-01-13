# OPERADORES IDENTIDAD
# is => es
# is not => no es
# Sirve para ver si estan apuntando a la misma dirección de memoria.
frutas = ['manzana', 'pera', 'fresa']
frutas2 = frutas
print(frutas is frutas2) # True

# OPERADORES DE PERTENENCIA
# in => me indicara si esta incluido o no en cierta collecion de datos
# not in
alumnos = ['Jose', 'Raul', 'Yomar', 'Gonzalo']
nombre = 'Yomar'
print(nombre not in alumnos)
