class Mueble: # Los parentesis son opcionales >> clas Mueble():
    tipo = 'Futon'
    valor = ""
    color = 'transparente'
    especificaciones = ['Hecho en Perú', 'Kaoba']
    # def >> definimos un metodo
    # self >> sirve como this en c#, java, devuelve atributos y metodos de la clase
    # si enviamos parametro podemos presindir de self
    # no necesariamente debe ser self, puede ser cualquier palabra pero es por buenas practicas
    def devolver_especs(self):
        return self.especificaciones

# instanciar o crear un objeto de la clase Mueble
mueble1 = Mueble()
mueble2 = Mueble()

mueble1.tipo = 'dos cuerpos'
espec2 = mueble2.devolver_especs()

print(mueble1.tipo)
print(mueble2.tipo)
print(espec2)
