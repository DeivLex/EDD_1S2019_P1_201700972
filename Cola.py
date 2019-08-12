class Cola:

    def __init__(self):
       
        # La cola vacía se representa por una lista vacía
        self.items=['','','','','','','','','','','','','','','','','','','','']

    def encolar(self, x,y):
    
        self.items.append(x)
        self.items.append(y)

    def desencolar(self):
        
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
    
        return self.items == []

    def imprimir(self):
        k=len(self.items)-1
        h=k-20
        while k > h :
         print(self.items[k])
         k-=1
