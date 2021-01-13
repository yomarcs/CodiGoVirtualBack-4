def saludar():
    """Función que te saluda"""
    print('Hola Yomar.... Bienvenido a Python!!')
saludar()

def saludarConNombre(nombre):
    print(f'Vamos {nombre}, tu puedes!!')
saludarConNombre('Yomar')

def saludoOpcional(apellido, nombre=None):
    if nombre:
        print(f'Hola {nombre} {apellido}')
    else:
        print(f'Hola {apellido}')
saludoOpcional("Cerdán")
saludoOpcional('Cerdán','Yomar')

def suma(num1,num2):
    return num1+num2
resultado = suma(4,5)
print(resultado) 

def hobbies(*args):
    print(args)
    for elemento in args:
        print(elemento)
hobbies("Bicicleta","Puenting",'Rafting',['Parapente',1,True],1,"2")

def persona(**Kwargs):
    print(Kwargs)
    for person in Kwargs:
        print(person)
persona(nombre='Yomar',apellido='Cerdán',edad=36,soltero=True   )

def indeterminado(*args, **Kwargs):
    print(args)
    print(Kwargs)
indeterminado('Yomar','Gabriel','Fabian',[1,2,3,],persona='Gabriel',apellido='Cerdán')

def pasaDeLargo():
    pass

resultado = lambda numero1, numero2: numero1 + numero2
print(resultado(2,4))