import time
class Pila:
    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
    def esta_vacia(self):
        return len(self.elementos) == 0
    def apilar(self, elemento):
        self.elementos.append(elemento)
    def desapilar(self):
        return self.elementos.pop()
    def imprimir(self):
        print(f"{self.nombre}: {self.elementos}")
        time.sleep(2)
def mover_disco(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} desde {origen.nombre} hasta {destino.nombre}")
    origen.imprimir()
    destino.imprimir()
    time.sleep(2)
def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        hanoi(n-1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        hanoi(n-1, auxiliar, origen, destino)
origen = Pila("Origen")
auxiliar = Pila("Auxiliar")
destino = Pila("Destino")
for disco in range(3, 0, -1):
    origen.apilar(disco)    
origen.imprimir()
auxiliar.imprimir()
destino.imprimir()
time.sleep(2)
hanoi(3, origen, auxiliar, destino)