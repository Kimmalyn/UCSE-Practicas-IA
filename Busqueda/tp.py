from simpleai.search.models import SearchProblem
from simpleai.search import astar, breadth_first, depth_first, greedy, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

TUNELES=MINA_L = (
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
    (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
)

ROBOTS = (("s1", "soporte",(5,1)), ("e1", "escaneador", (5,1), 1000), ("e2", "escaneador", (5,1), 1000))

INITIAL_STATE = ROBOTS,TUNELES

ESCANEADOS = []

ACCIONES_MOVER = [((-1, 0)),
                  ((1, 0)),
                  ((0, -1)),
                  ((0, 1))]

class robotsminerosproblem(SearchProblem):

    def is_goal(self, state):
        return len(state[1]) == 0
    
    def cost(self, state, action, state2):
        _, accion, _ = action
        #si la accion es cargar, el robot demora 5min
        if accion == "cargar":
            return 5
        else: #si la accion es mover, el robot demora 1min
            return 1
     
    def actions(self, state):
        acciones = []
        robots, tuneles = state
        #las acciones estarán conformadas por tupla de robot, acción que se va a realizar y destino o el  id del robot que recargara (dependiendo el tipo de accion)
        #las acciones disponibles son Mover y Cargar
        #el destino puede venir definido por una posicion (fila, columna) o por un id de robot escaneador 
        #("s1", "mover", (5, 1))
        #("s1", "cargar", "e2")
        descargados = False
        for robot in robots: 
            if  robot[1] == "escaneador":
                if robot[3]==0:
                    descargados = True

        #comienzo recorriendo los robots disponibles
        for robot in robots:
            #Si el robot es escaneador
            if robot[1] == "escaneador":
                #me guardo el id, la posicion y la bateria actual del robot
                id_robot, tipo_robot, posicion, bateria = robot

                #lo que hago es sacar la fila y columna en la que se encuentra el robot
                fila_robot, columna_robot = posicion

                #si la bateria actual es mayor que 100mAh, el robot se puede mover
                if bateria >= 100:               
                    # recorro las acciones_mover (arriba, abajo, derecha, izquierda), calculo la nueva posición y la agrego en acciones
                    for (fila, columna) in ACCIONES_MOVER:
                        nueva_fila = fila_robot + fila
                        nueva_columna = columna_robot + columna
                        posicion_destino = (nueva_fila, nueva_columna)
                        #si la nueva posicion esta en la lista de tuneles me puedo mover
                        if (posicion_destino in tuneles):
                            acciones.append((id_robot, "mover", posicion_destino))
                        elif (posicion_destino in TUNELES):
                            acciones.append((id_robot, "mover", posicion_destino))                
            else: #si el robot es de soporte
                if descargados:
                    #me guardo el id, la posicion y la bateria actual del robot
                    id_robot, tipo_robot, posicion = robot

                    #lo que hago es sacar la fila y columna en la que se encuentra el robot
                    (fila_robot, columna_robot) = posicion

                    #recorro la lista de robots
                    for robot_a_abastecer in robots:
                        #pregunto si la posicion del robot a abastecer es la misma que el robot de soporte
                        #si la bateria del robot a abastecer es menor a 1000 
                        # y si el roboy es tipo escaneador
                        if robot_a_abastecer[1] == "escaneador":                 
                            if (robot_a_abastecer[2] == posicion and (robot_a_abastecer [3] <= 100)):
                                #si cumple estas caracteristicas debo generar una acción de cargar
                                #en acciones cargo el id del robot de soporte, la accion y el id del robot escaneador que se abasteció
                                acciones.append((id_robot, "cargar", robot_a_abastecer[0]))
                            else:
                                #si no se cumple con las condiciones anteriores, el robot se debe mover
                                for (fila, columna) in ACCIONES_MOVER:
                                    nueva_fila = fila_robot + fila
                                    nueva_columna = columna_robot + columna
                                    posicion_destino = (nueva_fila, nueva_columna)
                                    #si la nueva posicion esta en la lista de tuneles me puedo mover
                                    if (posicion_destino in ESCANEADOS):
                                        acciones.append((id_robot, "mover", posicion_destino))
                                    elif (posicion_destino in TUNELES):
                                        acciones.append((id_robot, "mover", posicion_destino))    
        return acciones
    
# ("s1", "soporte", (5,1), 1000) <--- ESTADO DEL ROBOT

    def result(self, state, action):

        id_robot,accion_desc, accion = action

        robots,tuneles = state

        robots = list(robots)
        tuneles = list(tuneles)

        if accion_desc == "mover":
            #busco el robot a mover
            robot = [x for x in robots if x[0] == id_robot]
            robot = robot[0]
            robots.remove(robot)

            robotlist=list(robot)
            #muevo el robot
            robotlist[2]=accion
            #si es escaneador le resto bateria y pregunto si se mueve a un casillero no escaneado
            #si se mueve a un no escaneado lo saco de la lista de tuneles
            if robotlist[1]=="escaneador":
                robotlist[3]=robotlist[3]-100
                if accion in tuneles:
                    ESCANEADOS.append(accion)
                    tuneles.remove(accion)
            
            #robot = tuple(robotlist)    
            robots.append(tuple(robotlist))
        else:
            #si la accion es cargar busco el robot a cargar y lo saco de la lista
            #le relleno la bateria y lo vuelvo insertar
            robot = [x for x in robots if x[0] == accion]
            robot = robot[0]
            robots.remove(robot)

            robotlist=list(robot)
            robotlist[3]=1000

            #robot = tuple(robotlist)
            robots.append(tuple(robotlist))
        
        new_state = tuple(robots),tuple(tuneles)

        return new_state

    def heuristic(self, state):
        return super().heuristic(state)

problem = robotsminerosproblem(INITIAL_STATE)

result = astar(problem)

print(result.path)