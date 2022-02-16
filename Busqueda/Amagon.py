from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)

ALMACEN = ((r,c) for r in range(7) for c in range(6))

RACKS=[(0,0),(0,1),(0,2),
       (0,4),(0,5),(0,6),
       (2,0),(2,1),(2,3),
       (2,4),(2,5),(2,6),
       (4,0),(4,1),(4,3),
       (4,4),(4,5),(4,6),]

CAMINOROBOT = []

for celda in ALMACEN:
    if celda not in RACKS:
        CAMINOROBOT.append(celda)

INITIAL_STATE = ([(3,5),()],[(0,0),(0,5),(2,1),(4,0)])

ACCIONES_MOVER = [((-1, 0)),
                  ((1, 0)),
                  ((0, -1)),
                  ((0, 1))]

class Amagon(SearchProblem):
    def is_goal(self, state):
        return len(state[1]) == 0 and len(state[0][1]) == 0

    def cost(self, state, action, state2):
        return 1

    def actions(self, state):
        actions = []
        robot,cajas = state
        posicionrobot,cajascargadas = robot
        if posicionrobot == (3,5) and cajascargadas == 0 and len(cajas)!=0: #posiscion inicial
            if len(cajas)>2:
                cajascargadas.append(caja[-1])
                cajascargadas.append(caja[-1])
                actions.append(('cargar', robot))
            else:
                cajascargadas.append(caja[-1])
                actions.append(('cargar', robot))
        else:#robot cargado moviendose
            fila_robot,columna_robot = posicionrobot
            if posicionrobot not in cajascargadas:
                for (fila, columna) in ACCIONES_MOVER:
                        nueva_fila = fila_robot + fila
                        nueva_columna = columna_robot + columna
                        posicion_destino = (nueva_fila, nueva_columna)
                        #si la posicoion es valida                       
                        if (posicion_destino in CAMINOROBOT):
                            acciones.append(('mover', posicion_destino))
            else:
                acciones.append('descargar', robot)

        if posicionrobot != (3,5) and cajascargadas == 0 and len(cajas)!=0: #si se queda sin carga
            fila_robot,columna_robot = posicionrobot
            if posicionrobot not in cajascargadas:
                for (fila, columna) in ACCIONES_MOVER:
                        nueva_fila = fila_robot + fila
                        nueva_columna = columna_robot + columna
                        posicion_destino = (nueva_fila, nueva_columna)
                        #si la posicoion es valida                       
                        if (posicion_destino in CAMINOROBOT):
                            acciones.append(('mover', posicion_destino))
            
    def result(self, state, action):
        accion, robot = action
        statelist=list(state)

        if accion == 'mover':
            pass
        pass



    def heuristic(self, state):
        pass

