from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    greedy,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer

INITIAL_STATE = (((0,0),3,100),())

OBSTACULOS = [(0,1),(0,2),(1,4),(2,1),(3,1),(3,3),(4,3)]

ZOMBIES = [(1,0),(1,1),(1,2),(1,3),(2,3)]

GOAL_STATE = (4,4)

columns = list(range(5))
rows = list(range(5))
MAPA = [
    (row, col)
    for row in rows
    for col in columns
]

ACCIONES_MOVER = [((-1, 0)),
                  ((1, 0)),
                  ((0, -1)),
                  ((0, 1))]

class Zombies_Problem(SearchProblem):

    def is_goal(self, state):
        prota,_ = state
        posicion,_,_ = prota

        return posicion == GOAL_STATE
    
    def cost(self, state, action, state2):
        accion,_=action
        if accion == 'correr':
            return 10
        if accion == 'disparar':
            return 20
        if accion == 'rodear':
            return 30

    def actions(self, state):
        acciones = []
        prota,zombies = state
        posicion,balas,vida = prota
        if vida != 0:
            for (fila,columna) in ACCIONES_MOVER:
                nueva_fila = fila_robot + fila
                nueva_columna = columna_robot + columna
                posicion_destino = (nueva_fila, nueva_columna)
                if posicion_destino in MAPA and posicion_destino not in OBSTACULOS:
                    if posicion_destino in ZOMBIES and  posicion_destino not in zombies:
                        if balas != 0:
                            acciones.append('disparar',posicion_destino)
                        acciones.append('rodear', posicion_destino)
                    else:
                        acciones.append('correr', posicion_destino)

        return acciones

    def result(self, state, action):
        prota,zombies = state
        posicion,balas,vida = prota
        accion,posicion_nueva = action

        if accion == 'disparar':
            balas -= 1
            zombielist = list(zombies)
            zombielist.append(posicion_nueva)
        if accion == 'rodear':
            vida-=30

        new_prota=tuple(posicion_nueva,balas,vida)
        new_state = (new_prota,tuple(zombielist))

        return new_state

    def heuristic(self, state):
        return 80 #menor cantidad de costo  posible relajando el problema quitando obstaculos y zombies