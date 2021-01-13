class Vehiculo:
    def __init__(self, peso):
        self.peso = peso
    def movilidad(self):
        print('Me Muevo en muchas ruedas')

class Automovil(Vehiculo):
    def movilidad(self):
        print('Me muevo en 4 ruedas')

class Bicicleta(Vehiculo):
    def movilidad(self):
        print('Me muevo en 2 ruedas')

class Patines(Vehiculo):
    def movilidad(self):
        print('Me muevo en 8 ruedas')

objVehiculo = Vehiculo(45)
objVehiculo.movilidad()

objAutomovil = Automovil(17)
objAutomovil.movilidad()

objBicicleta = Bicicleta(16)
objBicicleta.movilidad()
 
objPatines = Patines(16)
objPatines.movilidad()

