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
        self.stack.pop() #elimina el ultimo elemento
        self.top = self.stack[-1]

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

mistack = stack()
mistack.add(1)
mistack.add(2)
mistack.add(3)
mistack.add(4)
mistack.add(5)
mistack.remove()
mistack.remove()
print(mistack)