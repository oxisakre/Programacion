class Hotel:
 """Representa un hotel: sus atributos son:
 nombre, ubicacion, puntaje y precio."""

def __init__(self, nombre, ubicacion, puntaje, precio):
        """Crea un Hotel.
        nombre y ubicacion deben ser cadenas no vacías,
        puntaje y precio son números."""
        self.nombre = validar_cadena_no_vacia(nombre)
        self.ubicacion = validar_cadena_no_vacia(ubicacion)
        self.puntaje = validar_numero_positivo(puntaje)
        self.precio = validar_numero_positivo(precio)

def __str__(self):
        """Conversión a cadena de texto."""
        return "{} de {} - Puntaje: {} - Precio: {} pesos".format(
        self.nombre,
        self.ubicacion,
        self.puntaje,
        self.precio,
        )

def ratio(self):
        """Calcula la relación calidad-precio de un hotel"""
        return ((self.puntaje ** 2) * 10) / self.precio