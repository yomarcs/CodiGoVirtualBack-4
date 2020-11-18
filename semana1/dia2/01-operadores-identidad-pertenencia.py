# OPERADORES IDENTIDAD
# is => es
# in not => no es
# Sirve para ver sis estan apuntando a la misma direccion de memoria.
frutas = ['manzana', 'pera', 'fresa']
frutas2 = frutas
print(frutas is frutas2)

# OPERADORES DE PERTENENCIA
# in => me indicara si esta incluido o no en cierta collecion de datos
# not in
alumnos = ['Jose', 'Raul', 'Cintia', 'Gonzalo']
nombre = 'Eduardo'
print(nombre not in alumnos)
