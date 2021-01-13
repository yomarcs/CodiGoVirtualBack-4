# Ingresar un numero por el teclado y que me diga si es mayor que 0 o menor que cero

# numero = int(input('Ingrese numero: '))
# if numero > 0:
#     print(f'{numero} es mayor a 0')
# elif numero < 0:
#     print(f'{numero} es menor a 0')
# else:
#     print(f'{numero} es igual 0')

texto = 'GOL DE PERÚ'
# for letra in texto:
    # print(letra)

for i in range(1,10,3):
    print(i)

print()

for i in range(len(texto)):
    print(f'posicion {i}: {texto[i]}')
print()

for i in range(10):
    print(i)
    if i == 5:
        break
print()

for i in range(10):
    if i == 5:
        continue
    print(i)
print()

# Ingresar 10 valores por teclado y almacenarlos en una lista y luego 
# que me diga cuantos pares y cuantos son impares

numeros=[]
numeroPar=0
numeroImpar=0
for i in range(10):
    numero = int(input(f'Ingrese el numero {i+1}: '))
    if numero % 2 == 0:
        numeroPar +=1
    else:
        numeroImpar +=1
    numeros.append(numero)
print(numeros)
print(f'Hay {numeroPar} números pares')
print(f'Hay {numeroImpar} números impares')