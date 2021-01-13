class Persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionaliddad = nacionalidad
    def saludar(self):
        print(f'Hola {self.nombre} {self.apellido}')

class Alumno(Persona):
    def __init__(self, num_matricula, anio, nombre, apellido, nacionalidad):
        self.matricula = num_matricula
        self.anio = anio
        super().__init__(nombre, apellido, nacionalidad)
    def mostrarAnio(self):
        print(f'Su año es {self.anio}')

objPersona = Persona('Yomar','Cerdán Sulca','nacionalidad')
objPersona.saludar()

objAlumno = Alumno(2015008,1996,'Kevin','Cerdán Sulca','Colombiano')
objAlumno.saludar()
objAlumno.mostrarAnio()
print(objAlumno.nacionaliddad)
   

        