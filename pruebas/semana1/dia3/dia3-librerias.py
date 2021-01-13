import camelcase

camello = camelcase.CamelCase()
texto = 'amo mucho a mis hijos'
# convierte a mayúscula la primera letra de cada palabra
print(camello.hump(texto)) # Amo Mucho a Mis Hijos.