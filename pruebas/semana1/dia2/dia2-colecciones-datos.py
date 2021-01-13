colores = ['rojo', 'blanco','azul','violeta']
print(colores)
print(colores[2])
print(colores[-1])
print(colores[-2])

print(colores[1:2])

colores2 = colores[:]
colores[0]='rojito'
print(colores)
print(colores2) 

nombre = 'Yomar'
print(nombre[3])

colores.append('negro')
print(colores)

colores.remove(colores[1])
print(colores)

colores.remove('negro')
print(colores)

colorEliminado = colores.pop(1)
print(colorEliminado)

colores.clear()
print(colores)

#############################################################

nombres = ('Yomar', 'Kevin', 'Gabriel', 'Fabian', 'Yomar')
print(nombres)
print(nombres[0])
print(len(colores2))
print(len(nombres))
print(nombres.count('Yomar'))

##############################################################

estaciones = {'Verano','Otoño','Invierno','Primavera',}
estaciones.add('OtoñoVerano')
print(estaciones)

###############################################################

persona = {
    'id': 1,
    'nombre':'Yomar',
    'relacion':'soltero',
    'hobbies':{
        'nombre':'futbol',
         'dificultad':'básico'
            }
}
print(persona)