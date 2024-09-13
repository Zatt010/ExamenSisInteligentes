# ******************************************************************
# * Clase: Entorno                                                 *
# * Autor: Victor Estevez                                          *
# * Version: v2023.03.29                                           *
# * Descripcion: Implementacion del entorno, proporciona           *
# *              percepciones a los agentes y ejecuta las acciones *
# *              de cada agente  que se encuentra en el            *
# ******************************************************************

class Entorno:
    def __init__(self):
        self.estado_actual = None
        self.estado_meta = None

    def set_estado_inicial(self, estado_inicial):
        self.estado_actual = estado_inicial

    def set_estado_meta(self, estado_meta):
        self.estado_meta = estado_meta

    def percepcion(self):
        return self.estado_actual

    def ejecutar_accion(self, accion):
        self.estado_actual = accion

    def test_objetivo(self):
        return self.estado_actual == self.estado_meta

    def genera_hijos(self, nodo):
        return [2 * nodo, 2 * nodo + 1]
