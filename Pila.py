class Pila:
    

    def __init__(self):
        
        # La pila vacía se representa con una lista vacía
        self.items=[]
    
    def apilar(self, x):
    
    # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    def es_vacia(self):
    
        return self.items == []
    def imprimir(self):
        print(self.items)

if __name__ == "__main__":
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.apilar("hola")
    print(p.es_vacia())
    p.desapilar()
    p.imprimir()