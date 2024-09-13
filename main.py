from AgenteIA.Entorno import Entorno
from AgenteIA.AgenteBuscadorDFS import AgenteBuscador

def main():
    entorno = Entorno()
    
    estado_inicial = 1
    estado_meta = 11
    entorno.set_estado_inicial(estado_inicial)
    entorno.set_estado_meta(estado_meta)
    
    agente = AgenteBuscador()
    
    agente.set_tecnica("profundidad")
    agente.set_estado_inicial(estado_inicial)
    agente.set_estado_meta(estado_meta)
    
    agente.add_funcion_sucesor(entorno.genera_hijos)
    
    agente.programa()
    
    print("Camino encontrado:", agente.acciones)

if __name__ == "__main__":
    main()

