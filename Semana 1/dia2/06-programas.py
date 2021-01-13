# Para usar solamente lo yo que desee y no usar toda la funcionalidad de la libreria
# from nomb_mod import Clase, fun, met... 
# from modulo import despedir, saludar

# En python si queremos usar un archivo que no se encuentra en nuestro mismo nivel sino que externo,
# se tendrá que agregar al PYTHONPATH (https://docs.python.org/es/3/tutorial/modules.html#the-module-search-path) 
# pero no es recomendable hacer eso si es que nuestro archivo solamente lo vamos a usar una sola vez.

import modulo

respuesta = modulo.despedir("Yomar")
respuestaBienvenida = modulo.saludar("Yomar")
print(respuestaBienvenida)
print(respuesta)

