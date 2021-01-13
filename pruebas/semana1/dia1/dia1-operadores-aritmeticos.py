num1, num2 = 29, 10
print(num1)
print(num2)
print("La suma es {}".format(num1 + num2))
print(f"La resta es {num1 - num2}")
print("La multipliación es {}".format(num1 * num2))
print("La división es {}".format(num1 / num2))
print(f"El módulo es {num1 % num2}")
print(f"EL cociente es {num1 // num2}")

var1 = 10
var2 = 20
var1 += var2
print(var1)

num1, num2 = 15, 25
print(num1 > num2)

print((10>=10) and (10>20)) # v and F >> False
print((10>=10) or (10>20)) # v or F >> True
print(not(10>=10) or (10>20)) # not(v or F >> True) >> False