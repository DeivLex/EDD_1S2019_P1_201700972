class Cola:

    def __init__(self):
       
        # La cola vacía se representa por una lista vacía
        self.items=[]

    def encolar(self, x):
    
        self.items.append(x)

    def desencolar(self):
        
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
    
        return self.items == []

    def imprimir(self):
        print(self.items)
