# Para definir variables numericas
numero = 1
numerodecimal = 18.5

# variables de tipo texto
texto = 'Soy un texto'
otrotexto = 'Soy otro texto'

# Para saber que tipo de variable es
type(texto)
print(type(numerodecimal))
# Para imprimir en consola se utiliza print()
print(1,2,3)

# Para definir una variable tiene que comenzar con una letra, nunca con un numero

# Hay dos clases de variables, cariables MUTABLES, variables INMUTABLES
# MUTABLES -> Son las variables que se van a modifoicar y todas sus 
# refrencias van a sufrir los cabios ( List, dict, tuples) 
# INMUTABLES -> Son las que se van a a modificar solamente una determinada variable si que la otras que copiaron su valortab lo hagan
# (int, str , float, bool, etc)

# Para eleiminar una variable
del texto

variable1 = 20
variable2 = 10.5
variable3 = True
variable4 = 'texto'

# Para definir varias variables en un sola linea de codigo
# nombre = Yomar apellido = Cerdán Sulca
nombre, apellido = 'Yomar', "Cerdán Sulca"
edad, nacionalidad = (35, "Peruano")
print(nombre)
print(apellido)
print(edad)
print(nacionalidad)

# La variable con valor None es una variable sin tipo y esta
# esperando cambiar de valor para tener un tipo definido
variablex = None

# Variables mutables
a=10
b=a
a=20
print(b,a)

# variables mutables
c=[10,15]
d = c
c[0] =15
print(d)
