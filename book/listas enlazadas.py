from primo import esprimo
class _Nodo:
    
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    """Modela una lista enlazada."""
    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0
    def __str__(self):
        String = "["
        Current = self.prim
        while Current != None:
            String += str(Current)
            String += str(", ")
            Current = Current.prox
        String += "]"

        return String

    def __len__(self):
        return self.len
    
    def append(self, dato):
        minodo = _Nodo(dato)

        if self.len == 0:
            self.prim = minodo
        else:
            Current = self.prim
            while Current.prox != None:
                Current = Current.prox
            Current.prox = minodo

        self.len +=1

        return minodo

    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")

        if i == 0:
        # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
        for pos in range(1, i):
            n_ant = n_act
            n_act = n_ant.prox

        # Guardar el dato y descartar el nodo
        dato = n_act.dato
        n_ant.prox = n_act.prox

        self.len -= 1
        return dato
    def remove(self, dato):
        if self.prim == None:
            return False
        if self.prim.dato == dato:
            self.prim = self.prim.prox
        else:
            current = self.prim
            while current.prox is not None and current.prox.dato != dato:     ### esta es la linea es la modificada
                current = current.prox
            
            if current.prox is None:  ### si el siguiente elemento era el ultimo, entonces no está el elemento, devolvemos falso
                return False
            
            deletedNode = current.prox
            current.prox = deletedNode.prox

            self.len = self.len - 1
            return True
    def remove_todos(self, dato):
        current = second = self.prim
        contador = 0
        if second == dato:     # no remueve el primero vaya a saber dios por que
            second = second.prox
            contador += 1
        
        while current is not None:
            while second.prox is not None:   # check second.next here rather than second
                if second.prox.dato == dato:   # check second.next.data, not second.data
                    second.prox = second.prox.prox # cut second.next out of the list
                    contador += 1               
                else:
                    second = second.prox   # put this line in an else, to avoid skipping items
            current = second = current.prox

        return print('veces eliminadas del nodo:', contador)

    def duplicar(self, dato):
        
        current = self.prim
    
        while current is not None:
            if current.dato == dato:  #lo hace solo una vez y con el while explota
                minodo = _Nodo(dato)
                minodo.prox = current.prox
                current.prox = minodo
                current = minodo.prox
                self.len +=1
            else:
                current = current.prox
                
        
    def insert(self, i, x):
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""

        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")

        nuevo = _Nodo(x)

        if i == 0:
        # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
        # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
        for pos in range(1, i):
            n_ant = n_ant.prox

        # Intercalar el nuevo nodo
        nuevo.prox = n_ant.prox
        n_ant.prox = nuevo

        self.len += 1
    
    def countPrime(self):
     
        lista = ListaEnlazada()
        ptr = self.prim
        current = lista.prim

        while ptr != None:
            # If current node is prime
            if esprimo(ptr.dato):
                if lista.len == 0:
                    lista.prim = _Nodo(ptr.dato)
                    current = lista.prim
                    lista.len += 1
                else:
                    current.prox = _Nodo(ptr.dato)
                    current = current.prox
                    lista.len += 1
            ptr = ptr.prox
        return lista

    def reversa(self):
        anterior = None
        current = self.prim
        while current is not None:
            siguiente = current.prox
            current.prox = anterior
            anterior = current
            current = siguiente
        self.prim = anterior
       
    def extend(self, lista):
        minodo = lista.prim
        
        if self.len == 0:
            self.prim = minodo
        else:
            Current = self.prim
            while Current.prox != None:
                Current = Current.prox
            Current.prox = minodo

        self.len += lista.len



milista = ListaEnlazada()
milista.append(5)
milista.append(8)
milista.append(7)
milista.append(3)
milista.append(37)
milista.append(40)
milista.reversa()
print(milista)

