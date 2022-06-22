class queue:
    def __init__(self):
        self.initial = None
        self.final = None
        self.queue = []

    def getinitial(self):
        return self.initial

    def getfinal(self):
        return self.final

    def add(self, element):
        self.queue.append(element)
        self.final = element
        return self.final

    def remove(self):
        self.queue.pop(0)
        self.initial = self.queue[0]
        return self.initial

    def __str__(self):
        return str(self.queue)
    
    def __len__(self):
        return len(self.queue)

micola = queue()
micola.add(1)
micola.add(2)
micola.add(3)
micola.add(4)
micola.add(5)
micola.remove()
micola.remove()
micola.remove()
print(micola)
