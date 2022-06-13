

class Intervalo:

    def __init__(self, desde, hasta):
        if hasta < desde:
            raise ValueError ('desde debe ser menor que hasta') 
        self.desde = desde
        self.hasta = hasta

    def duracion(self):
        return self.hasta - self.desde

    def interseccion(self, intervalo):
                
        if (self.hasta <= intervalo.desde) or (self.desde >= intervalo.hasta):
            raise ValueError('no hay interseccion')
        
        inter_hasta = min(self.hasta, intervalo.hasta)
        inter_desde = max(self.desde, intervalo.desde)
        
        return Intervalo(inter_desde, inter_hasta)

    def union(self, intervalo):
        
        if (self.hasta < intervalo.desde) or (self.desde > intervalo.hasta):
            raise ValueError('no hay interseccion')
        
        inter_hasta = max(self.hasta, intervalo.hasta)
        inter_desde = min(self.desde, intervalo.desde)
        return Intervalo(inter_desde, inter_hasta)


intervalo1 = Intervalo(1, 6)
intervalo2 = Intervalo(5, 10)
interseccion = intervalo1.interseccion(intervalo2)
assert interseccion.desde == 5

        

        
    
    

