class Hotel:
    """Representa un hotel: sus atributos son:
        nombre, ubicacion, puntaje y precio."""


    def __init__(self, nombre, ubicacion, puntaje, precio):
        """Crea un Hotel.
        nombre y ubicacion deben ser cadenas no vacías,
        puntaje y precio son números."""
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.puntaje = puntaje
        self.precio = precio


    def __str__(self):
        """Conversión a cadena de texto."""
        return "{} de {} - Puntaje: {} - Precio: {} pesos".format(
            self.nombre,
            self.ubicacion,
            self.puntaje,
            self.precio,
        )


    def __lt__(self, hotel):
        ubi = self.ubicacion < hotel.ubicacion
        if self.ubicacion != hotel.ubicacion:
            return ubi

        return self.ratio() < hotel.ratio()  
        


    def ratio(self):
        """Calcula la relación calidad-precio de un hotel"""
        return ((self.puntaje ** 2) * 10) / self.precio

h = Hotel("Hotel City", "Mercedes", 3.25, 78)
i = Hotel("Hotel Mascardi", "Mercedes", 6, 150)
j = [i, h]
j.sort()
print(str(j[0])),print('---') , print(str(j[1]))
print(i.ratio(), h.ratio())
