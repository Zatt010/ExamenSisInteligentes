from AgenteIA.Agente import Agente
import copy

class AgenteBuscador(Agente):

    def __init__(self):
        Agente.__init__(self)
        self.funcionSucesor = []
        self.tecnica = None
        self.estadoInicial = None
        self.estadoMeta = None
        self.acciones = None
        self.profundidad_maxima = 10

    def set_tecnica(self, t):
        self.tecnica = t

    def set_estado_inicial(self, e0):
        self.estadoInicial = e0

    def set_estado_meta(self, ef):
        self.estadoMeta = ef

    def add_funcion_sucesor(self, fun):
        self.funcionSucesor.append(fun)

    def test_objetivo(self, nodo):
        return nodo == self.estadoMeta

    def genera_hijos(self, nodo):
        return self.funcionSucesor[0](nodo) if self.funcionSucesor else []

    def programa(self):
        frontera = [[self.estadoInicial]]
        visitados = set()
        cont = 0
        
        while frontera:
            cont += 1
            camino = frontera.pop()
            nodo = camino[-1]

            if len(camino) > self.profundidad_maxima:
                continue 
            
            print(f"Visitando nodo: {nodo}, camino: {camino}")

            if self.test_objetivo(nodo):
                self.acciones = camino
                print(f"Estado objetivo encontrado: {nodo}")
                break
            else:
                visitados.add(nodo)
                for hijo in self.genera_hijos(nodo):
                    if hijo != 0 and hijo not in visitados:
                        aux = camino[:]  
                        aux.append(hijo)
                        frontera.append(aux)

            if not frontera:
                print("No se encontró una solución.")
                break
