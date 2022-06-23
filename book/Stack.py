class stack:

    def __init__(self):
        self.top = None
        self.stack = [] 

    def getTop(self):
        return self.top

    def add(self, element):
        self.top = element
        self.stack.append(element)
        

    def remove(self):
        if len(self.stack) == 0:
            raise IndexError("La pila está vacía")
        
        self.stack.pop() #elimina el ultimo elemento
        self.top = self.stack[-1]

        

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

mistack = stack()

mistack.remove()

print(mistack)