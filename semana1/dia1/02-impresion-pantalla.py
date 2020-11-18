codigo = 'virtual4'
# El metodo print va a recoger un numero ilimitado de parametros separados
# por "," y aiempre entre coma y coma va a imprimir un espacio en blanco
print(codigo, "otra cosa")

# MODO 2
alumnos = 38
print("Estoy en el curso {} y hay {} alumnos".format(codigo, alumnos))

# MODO III Modificando el orden a imprimir
print("Tengo {1} alumnos del curso {0}".format(codigo,alumnos) )

# Modo IV
print(f"tengo {alumnos} alumnos en el curso {codigo}")

# MODO V restringir la cantidad de decoimales de una variable
pi = 3.141515669645962349569
print(f"El valir de pi es: {pi:1.3f}")
