#Reynaldo Kama Copa 
# no tengo grupo. "nadie me quiere :("
"""1.- Implementar una funcion que permita expandir nodos hijos para n caracteres, los cuales deben ser 
establecidos al momento de iniciar el programa."""


class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
        
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())
    
    

def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0) #FIFO - cola (el primero en entrar es el primero en salir)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(len(estado_inicio)-1):
                for j in range(len(estado_inicio)-1): 
                    hijo_datos = nodo_actual.get_datos().copy()    
                    temp = hijo_datos[j]
                    hijo_datos[j] = hijo_datos[j+1]
                    hijo_datos[j+1] = temp
                    hijo = Nodo(hijo_datos)
                    if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                        nodo_actual.set_hijo(hijo)
                        nodos_frontera.append(hijo)
                        


import time

if __name__ == "__main__":
    estado_inicial = [2, 1, 3, 5, 4, 8, 6, 7, 9, 10]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end =time.time()
    print('Tiempo de ejecucion : ',end-start, 'seg.','\n')
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("------"*10)
    print('recorrido : \n')
    for i in range(len(resultado)):
      print(resultado[i])


"""2.- Describir cual es el nivel maximo de numero de digitos que el rompecabezas se puede resolver en 
su maquina, explicando a que se deberia este limite y como se lo podria superara."""
#Respuesta: 
"""     al poner como estado inicial el caso mas crítico mi máquina solo resuelve hasta el 7 caracteres en 
aproximadamente 40 min, 8 caracteres ya no resuelve se cuelga.
- Se debe a que los nodos crecen exponencialmente y llega a un punto en que la máquina ya no tiene la capacidad
en la memoria para seguir expandiendo
- Solución: otro tipo de algoritmos o trabajar en una máquina que tenga una alta capacidad de rendimiento.
"""