class Mueble:
    tipo = 'futon'
    valor = '' 
    color = 'negro'
    especificaciones = ['Hecho en Perú','Cedro']
    def devolver_especs(self):
        return self.especificaciones

mueble1 = Mueble()
mueble1.tipo = 'familiar'
mueble1.valor = 500
mueble1.especificaciones = ['Hecho en Perú','2da mano','2009']
print(mueble1.especificaciones)

print()

mueble2 = Mueble()
mueble2.especificaciones.append('3era mano')
print(mueble2.devolver_especs())

