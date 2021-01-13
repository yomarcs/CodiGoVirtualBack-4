# Crear un clase persona que tenga de atributos sus datos personales y su experiencia laboral,
# que ingrese un menu que ingrese en la opc 1 pra ingresar nueva experiencia, que la opc 2 
# la muestre y que la opcion 3 la elimine todas las experiencias


class Persona:
    def __init__(self, nombre, apellido, edad, fecnac):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecnac
        self.experiencias = []
    def ingreseExperiencia(self, experiencia):
        self.experiencias.append(experiencia)
    def imprimirExperiencias(self):
        print('Tus experiencias son: ',self.experiencias)
    def eliminarExperiencias(self):
        self.experiencias.clear()

objPersona = Persona('Yomar','Cerdán Sulca', 36, '12/09/84')
opcion = 0
while opcion != 4:       
    try:
        opcion = int(input("""========== Menú ==========
1. Ingrese experiencia
2. Mostrar experiencias
3. Eliminar experiencias
4. Salir
==========================
"""))
        if opcion == 1:
            experiencia = input('Ingrese experiencia: ')
            objPersona.ingreseExperiencia(experiencia=experiencia)
        elif opcion == 2:
            objPersona.imprimirExperiencias()
        elif opcion == 3:
            objPersona.eliminarExperiencias()
        elif opcion == 4:
            print('Adios')
        else:
            print('Ingrese opción valida')
    except:
        print('Ingrese números!!')
        print()

        