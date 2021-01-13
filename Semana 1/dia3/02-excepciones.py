# https://www.tutorialsteacher.com/python/error-types-in-python#:~:text=Python%20%2D%20Error%20Types,usually%20along%20with%20the%20reason.

# excepciones => try ...  except ... *** else ... finally ...

try:
    # todo el codigo que sea descrito adentro tendra un manejo
    # por si sucede algo malo, y si sucede algo malo el except
    # va a evitar que el programas se cuelgue
    numero1 = int(input("Ingrese un número: "))
    numero2 = int(input('Ingrese un segundo numero: '))
    print(numero1/numero2)
except ZeroDivisionError:
    print('No puede ingresar 0 como divisor')
except ValueError:
    print('Ingresa numeros y no letras')
except:
    print(EnvironmentError)
    print('Algo debiste haber hecho mal, intenta nuevamente!!!')
else:
    # Ingresa al else cuando no ingreso a ningun except
    print('Todo funciono correctamente')
finally:
    # No le importa si todo salio bien o si hubo error
    print('Yo me ejecuto si o si')

print('Yo soy otra parte del codigo')

# ==============================================================

x=0
arreglo = []
while x<10:
    try: 
        num = int(input('Ingrese un numero: '))
        arreglo.append(num)
        x = x + 1
    except:
        print('Ingrese un número!!')


