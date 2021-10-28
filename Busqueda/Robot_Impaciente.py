from abc import abstractproperty
from itertools import chain,combinations
from types import LambdaType, new_class
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer
from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    greedy,
    limited_depth_first,
    iterative_limited_depth_first,
    astar,
)
INITIAL_STATE=(0,0) #Posicion del robot

columns = list(range(6))
rows = list(range(6))
LABERINTO = [
    (row, col)
    for row in rows
    for col in columns
]

PAREDES = [(0,1),(1,1),(1,4),(2,3),(3,1),(3,2),(3,5,),(4,0),(4,2),(4,4),(5,2),(5,3)]

for celda in PAREDES:
    if celda in LABERINTO:
        LABERINTO.remove(celda)


ACCIONES_MOVER = [((-1, 0)),
                  ((1, 0)),
                  ((0, -1)),
                  ((0, 1))]

class RobotImpaciente(SearchProblem):

    def is_goal(self, state):
        return state == (5,5)

    def cost(self, state, action, state2):
        #si la accion es moverse por el laberinto devuelvo 10
        #si la accion es atravesar una pared devuelvo 20
        if action[0] == 'mover':
            return 10
        return 20

    def actions(self, state):
        #busco una nueva posicion para el robot y pregunto si esta es laberinto o pared
        #indico el tipo de accion y la posicion a la cual me tengo que mover
        posible_actions = []
        fila_robot,columna_robot = state
        for (fila, columna) in ACCIONES_MOVER:
            nueva_fila = fila_robot + fila
            nueva_columna = columna_robot + columna
            posicion_destino = (nueva_fila, nueva_columna)
            if posicion_destino in LABERINTO:
                posible_actions.append(('mover', posicion_destino))
            if posicion_destino in PAREDES:
                posible_actions.append(('atravesar', posicion_destino))
        
        return posible_actions

    def result(self, state, action):
        
        return action[1]

    def heuristic(self, state):
        #(1,1) -> (5,5) 5-1 = 2 | 5-2 = 3
        #cuento los pasos que faltan para llegar a la meta y lo multiplico por el costo menor
        if state ==(5,5):
            return 0
        fila,columna = state
        estimacion = ((5-fila)+(5-columna))*10
        return estimacion
        
METHODS = (
    #breadth_first, 
    #depth_first, 
    #uniform_cost,
    #greedy,
    #limited_depth_first,
    #iterative_limited_depth_first,
    astar,
)    
        
for search_algorithm in METHODS:
    print()
    print('=' * 50)
    print("Running:", search_algorithm)
    visor = BaseViewer()
    problem = RobotImpaciente(INITIAL_STATE)
    result = search_algorithm(problem, graph_search = True, viewer = visor)
    print ('Final State:', result.state)
    print('=' * 50)
    print(' - Statistics:')
    print(' - Amount of actions until goal:', len(result.path()))
    print(' - Raw data:', visor.stats)

    for action, state in result.path():
        print("   - Action:", action)
        print("   - Resulting State:", state)

