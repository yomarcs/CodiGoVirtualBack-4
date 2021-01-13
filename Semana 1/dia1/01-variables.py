# Para imprimir en consola se utiliza print()
# El metodo print va a recoger un numero ilimitado de parametros separados
# por "," y siempre entre coma y coma va a imprimir un espacio en blanco
print(1,2,3)

# Para definir variables numéricas
numero = 1 # Variable int
numerodecimal = 18.5  # Variable float

# variables de tipo texto
texto = 'Soy un texto'  # Variable String
otrotexto = "Soy otro texto" # Variable String

# variables booleanas
# Notar que empiezan en mayúscula
varBoolTrue = True 
varBoolFalse = False

# Para saber que tipo de variable es
type(texto)

# Imprisión de los tipos de variable
print(type(numero))
print(type(numerodecimal))
print(type(texto))
print(type(varBoolFalse))

# Para eliminar una variable
del texto
# print(texto) # NameError: name 'texto' is not defined

# Para definir varias variables en un sola linea de código
nombre, apellido = 'Yomar', "Cerdán Sulca"
edad, nacionalidad = (35, "Peruano")
print(nombre)
print(apellido)
print(edad)
print(nacionalidad)

# La variable con valor None es una variable sin tipo y esta
# esperando cambiar de valor para tener un tipo definido
variablex = None
variablex = True 
print(variablex)

# Para definir una variable tiene que comenzar con una letra, nunca con un número

# Hay dos clases de variables, variables MUTABLES y variables INMUTABLES
# MUTABLES >> Son las variables que se van a modificar y todas sus 
#             refrencias van a sufrir los cambios ( List, dict, tuples)
#             list >> listas (arrays)
#             dict >> dicionarios
#             tuples >> tuplas >> lista inmutable
# INMUTABLES >> Son las que se van a modificar solamente una determinada 
#               variable sin que las otras que copiaron su valor tb lo hagan
#               (int, str , float, bool, etc)

# Variables Inmutables
a=10
b=a
a=20
print(b,a) # Imprimira 10, 20

# variables Mutables
c=[10,15] # lo que es array en javascript, en python es lista(list)
d = c
c[0] =15
print(d) # Imprimira [15,15]
