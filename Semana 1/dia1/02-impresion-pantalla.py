# El metodo print va a recoger un numero ilimitado de parametros separados
# por "," y siempre entre coma y coma va a imprimir un espacio en blanco
codigo = 'virtual4'
alumnos = 38

# MODO 1
print(codigo, "otra cosa")

# .format >> convierte las variables a string para poder imprimirlas

# MODO 2
print("Estoy en el curso {} y hay {} alumnos".format(codigo, alumnos))

# MODO 3 - Modificando el orden a imprimir
print("Tengo {1} alumnos del curso {0}".format(codigo,alumnos) )

# Modo 4
print(f"tengo {alumnos} alumnos en el curso {codigo}")

# MODO 5 - restringir la cantidad de decoimales de una variable
pi = 3.141515669645962349569
print(f"El valir de pi es: {pi:1.3f}")
