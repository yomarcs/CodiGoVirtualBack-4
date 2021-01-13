class Persona:
     # __init__ >> Constructor
    def __init__(self, nombre, fecnac):
        self.nombre = nombre
        self.fecha_nacimiento = fecnac
    def saludar(self):
        print(f'hola {self.nombre}')
    def fechaNacimiento(self):
        print(f'Tu fecha de Nacimiento es  {self.fecha_nacimiento}')

persona1 = Persona('Yomar', '12 de setiembre de 1984')
persona1.saludar()
persona1.fechaNacimiento()

# Crear un clase persona que tenga de atributos sus datos personales y su experiencia laboral,
# que ingrese un menu que ingrese en la opc 1 pra ingresar nueva experiencia, que la opc 2 
# la muestre y que la opcion 3 la elimine todas las experiencias

class PersonaEjercicio:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.experiencias = []
    def ingresar_experiencia(self, experiencia):
        self.experiencias.append(experiencia)
    def mostrar_experiencias(self):
        print("Las experiencias son : ",self.experiencias)
    def eliminar_experiencias(self):
        self.experiencias.clear()

objPersona = PersonaEjercicio('Yomar', 'Cerdán', "36")
opcion = 0
while opcion != 4:
    try:
        opcion = int(input("""------- Menu ------
        1. Ingrese Experiencia
        2. Mostrar experiencia
        3. Eliminar todas las experiencias
        4. salir
        ---------------------
        """))
        if opcion == 1:
            experiencia = input ('Ingrese experiencia: ')
            objPersona.ingresar_experiencia(experiencia=experiencia)
        elif opcion == 2:
            objPersona.mostrar_experiencias()
        elif opcion == 3:
            objPersona.eliminar_experiencias()
        elif opcion == 4 :
            print('Adios')
        else:
            print('Ingresa opciones del 1 al 5')
    except:
        print('Ingrese solo numeros!!!')




# class Yomar:
#     expLaboral = []
#     def __init__(self, nombre, apellido, edad, explaboral):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.explaboral = explaboral
#     def agregarExperiencia(self):
#         exp = input(print('Ingresa nueva experiencia: ')   
#         expLaboral.append(exp)
#     def menu(self):
#         opcion = input(print('======== Menu ========')
#                        print(1. Ingrese nueva experiencia laboral)
#                        print(2. Imprimir experiencias)
#                        print(3. Eliminar experiencia)
#                        print(4. salir)
#                        print("Ingresa opcion : "))

# while opcion != 4


    
