# Función que no recibe parametros
def saludar():
    """Funcion que te Saluda"""
    print("Hola Yomar... Bienvenido a Python")
saludar()

# Las funciones pueden recibir cuantos parametros queramos
def saludarConNombre(nombre):
    print(f"hola {nombre}... vamos tu puedes!")
saludarConNombre('Yomar')

# Si queremos que un parametro sea opcional de dar su valor, le
# podemos definir el valor Predeterminado al momento de definir la funcion
def saludoOpcional(apellido, nombre=None):
    if nombre:
        print(f"hola {nombre} {apellido}")
    else:
        print("Hola Incognito")
    
saludoOpcional('Cerdán')
saludoOpcional('Cerdán', 'Yomar')

def suma(num1, num2):
    """Funcion que recibe 2 numeros y retorna la sumatoria"""
    return num1 + num2
#Todo lo que tengamos despues del return no se va a ejecutar
    # print('Hola')

resultado = suma(5,2)
print(resultado)

# el parametro *args arguments es una lista dinamica de elementos
# para recibir un numero indeterminado de parametros
def hobbies(*args):
    print(args)
    for elemento in args:
        print(elemento)

hobbies('bicicleta', 'puenting', 'rafting', 20, ['1',2, 3])

# **kwargs "Keywords arguments" es un parametro para recibir un numero ilimitado
# de parametro pero usando llave y valor(diccionario)
def personas(**kwargs):
    print(kwargs)

personas(nombre='Yomar', apeliido='Cerdán', mascotas=False, estatura=1.70)

def indeterminado( *args, **kwargs):
    print(args)
    print(kwargs)

indeterminado(5, 'Yomar', 'Otoño', False, pais='Perú',epoca='republicana')

# cuando colocamos la palabra reservada "pass" podemos pasar o obviar
# la lógica de la funcion definida
def sacar_igv(igv):
    pass

# FUNCIONES LAMBDA
# pequeña y anonima
# NombreFuncion = lambda param: return(rpta)
resultado = lambda numero: numero+30
resultado2 = lambda numero1, numero2: numero1+numero2
print(resultado(10))
print((resultado2(80,20)))
# Generalmente se utiliza para operaciones cortas de un maximo de una linea de resolucion
