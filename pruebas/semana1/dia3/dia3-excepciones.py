
try:
    numero1 = int(input('Ingrese número: '))
    numero2 = int(input('Ingrese segundo número: '))
    print(numero1/numero2)
except ZeroDivisionError:
    print('No puedes ingresar 0 como divisor')
except ValueError:
    print('Ingresa números, no letras!')
except:
    print('Este except es por si el usuario encuentra algun error no contemplado')
else:
    print('Todo salio bien!')
finally:
    print('Este mensaje se imprime si o si')

print('El programa sigue su camino por aqui......')

