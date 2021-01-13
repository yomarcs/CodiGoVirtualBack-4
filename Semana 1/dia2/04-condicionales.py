# Condicional IF ELSE ELIF
edad = 36
restriccion = 18
if edad >= restriccion  and edad < 65: 
    print('eres mayor de edad')
elif edad >= 65:
    print('Estas Jubilado')
else:
    print('Eres menor de edad')

# ELIF sirve para usarse en casos de case switch ( Python no existe en SWITCH CASE)

# Ingresar un numero por el teclado y que me diga si es mayor que 0 o menor que cero

numero = int(input('Ingrese numero: '))
if numero > 0:
    print(f'{numero} en mayor a 0')
elif numero < 0:
    print(f'{numero} es menor a 0')
else:
    print(f'{numero} es igual a 0')

# FOR => es para hacer un buclee repetitivo
texto = "GOL DE PERU"
for letra in texto:
    print(letra)
print() # linea en blanco
# for (let i=0; i<10; i++)
for i in range(1,10,3):
    print(i)
# El metodo range recibe de 1 a 3 valores
# 1: es el tope para la iteracion
# 2: el primro es el inicio y el segundo es el tope
# 3: el primero es el inicio y el segundo es eñ tope y el tercero
#    es cuando se va a incrementar o decrementar el ciclo

for i in range(len(texto)):
    print("posicion {}: {}".format(i, texto[i]))
#   posicion 0 : G
#   posicion 1 : O

# break => para parar el bucle
for i in range(10):
    print(i)
    if i == 5:
        break


# continue => salta la iteracion actual
for i in range(10):
    if i == 5:
        continue
    print(i)

# while >> es un bucle infinito hasta que la condicion deje de ser cierta
variable = True
while True:
    print('a')
    variable False
# En python no hay do ni switch case

# Ingresar 10 valores por teclado y almacenarlos en una lista y luego 
# que me diga cuantos pares y cuantos son impares
numeros = []
numeroPar = 0
numeroImpar = 0
for i in range(10):
    numero = int(input('Ingrese el numero {} : '.format(i+1)))
    if numero % 2 == 0:
        numeroPar += 1
    else:
        numeroImpar += 1
    numeros.append(numero)
print('hay {} numeros pares'.format(numeroPar))
print('hay {} numeros imppares'.format(numeroImpar))

# OPERADOR TERNARIO
# resultado = rpta_si if condicion  else rpta_no
# resultado = 5 if 11 % 2 == 0 else 10
# print(resultado)

