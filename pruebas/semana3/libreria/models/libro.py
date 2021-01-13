# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
# https://docs.sqlalchemy.org/en/13/core/type_basics.html
# nullable >> Para no admitir valores nulos. 

from base_de_datos import bd

class LibroModel(bd.Model):
    __tablename__ = 't_libro' # Cambia nombre de la tabla, sin esta linea la tabla se llamaria LibroModel
    id_libro = bd.Column('lib_id', bd.Integer, primary_key = True, autoincrement = True, nullable = False)
    nombre_libro = bd.Column('lib_nom', bd.String(45))
    edicion_libro = bd.Column('lib_edicion', bd.Date, nullable = False)
    autor_libro = bd.Column('lib_autor', bd.Text, nullable = False)
    cantidad_libro = bd.Column('lib_cant', bd.Integer, nullable = False)
    estado = bd.Column(bd.Boolean, default=True, nullable=False)
    # Sirve para hacer la relación inversa
    prestamosLibro = bd.relationship('PrestamoModel', backref='libroPrestamo')

    # Constructor >> Nos servira para trabajar los Controller
    def __init__(self, nombre, edicion, autor, cantidad):
        self.nombre_libro = nombre
        self.edicion_libro = edicion
        self.autor_libro = autor
        self.cantidad_libro = cantidad
    
    def save(self):
        # Crea la instanciación en la base de datos (ingresa sus datos pero aun no se guardan)
        bd.session.add(self)
        # Hace que los cambios ingresados  sean permanentes (aca ya de guarda en la base de datos)
        bd.session.commit()

    def __str__(self):
        # Este metodo mágico permite sobreescribir la forma en la cual se lee el objeto en consola
        return self.nombre_libro

    def devolverJson(self):
        return {
            'id':self.id_libro,
            'nombre':self.nombre_libro,
            'autor':self.autor_libro,
            'edicion':str(self.edicion_libro),
            'cantidad':self.cantidad_libro,
            'estado':self.estado
        }

    def devolverLibroPrestamo(self):
        resultado = self.devolverJson()
        prestamos = []
        for prestamo in self.prestamosLibro:
            # Cada vuelta va a devolver el prestamo segun su libro, si no hubiera ningun prestamo no me devuelve nada
            prestamos.append(prestamo.devolverJson())
        resultado['prestamos']=prestamos
        return resultado

    def update(self, **kwargs):
        # El metodo get se usa para los diccionarios y se encarga de que de acuerdo a la llave que le pasemos(parametro 1) va a devolver su valor y opcionalmente como segundo parametro qu ele puede indicar que va valor va a retornar si es que la llave indicada no existe
        # Operador ternario
        # resultado = True if condicion else False
        nombre = kwargs.get('nombre') if kwargs.get('nombre') else self.nombre_libro
        autor = kwargs.get('autor') if kwargs.get('autor') else self.autor_libro
        edicion = kwargs.get('edicion') if kwargs.get('edicion') else self.edicion_libro
        cantidad = kwargs.get('cantidad') if kwargs.get('cantidad') else self.cantidad_libro
        estado = kwargs.get('estado') if kwargs.get('estado') else self.estado
        # nombre = kwargs.get('nombre',self.nombre_libro)
        # autor = kwargs.get('autor',self.autor_libro)
        # edicion = kwargs.get('edicion',self.edicion_libro)
        # cantidad = kwargs.get('cantidad',self.cantidad_libro)
        self.nombre_libro = nombre
        self.autor_libro = autor
        self.edicion_libro = edicion
        self.cantidad_libro = cantidad
        self.estado = estado
        self.save()

    def delete(self):
        bd.session.delete(self)
        bd.session.commit()

    def inhabilitarLibro(self):
        self.estado=False
        self.save()
        # bd.session.commit()
    
