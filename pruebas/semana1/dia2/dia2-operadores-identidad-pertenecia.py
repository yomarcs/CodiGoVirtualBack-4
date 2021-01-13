# OPERADORES IDENTIDAD
# is => es
# in not => no es
# Sirve para ver si estan apuntando a la misma direccion de memoria.
frutas = ['manzana', 'pera', 'fresa','platano']
frutas2=frutas
# print(frutas2 is not frutas)

# OPERADORES DE PERTENENCIA
# in => me indicara si esta incluido o no en cierta collecion de datos
# not in
alumnos = ['Jose', 'Raul', 'Yomar', 'Gonzalo']
nombre = 'Yomar'
print(nombre in alumnos)