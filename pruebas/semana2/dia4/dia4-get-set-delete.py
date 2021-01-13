class Persona:
    def __init__(self):
        self.__nombre = ''
    def __getNombre(self):
        print('se ha ejecutado getNombre()')
        return self.__nombre
    def __setNombre(self, nombre):
        print('se ha ejecutado setNombre()')
        self.__nombre = nombre
    def __deleteNombre(self):
        print('Se ha ejecutado deleteNombre()')
        del self.__nombre
    name = property(__getNombre,__setNombre,__deleteNombre)

objPersona = Persona()
objPersona.name = 'Yomar'
print(objPersona.name)
del objPersona.name