class Vehiculo:
    def __init__(self, largo, ancho, peso):
        self.largo = largo
        self.ancho = ancho
        self.peso = peso
        self.__enMarcha = False
    def modificaMarcha(self):
        self.__enMarcha = True
    def __modificaLargo(self):
        self.largo = 0

objVehiculo = Vehiculo(15.00, 2.00, 2500)
objVehiculo.modificaMarcha()
objVehiculo.largo = 13.00
# objVehiculo.__modificaLargo()
