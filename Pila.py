class Pila:
    

    def __init__(self):
        
        # La pila vacía se representa con una lista vacía
        self.items=[]
    
    def apilar(self, x, y):
    
    # Apilar es agregar al final de la lista.
        self.items.append(x)
        self.items.append(y)

    def desapilar(self):
        
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    def es_vacia(self):
    
        return self.items == []
    def imprimir(self):
        print(self.items)

    def vaciar(self):
        self.items = []
