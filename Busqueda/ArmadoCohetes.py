from abc import abstractproperty
from itertools import chain,combinations
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

INITIAL_STATE = ("deposito", ((10,7),(15,3),(20,1),(5,0.5),(5,1.5)),())

class ArmadoCohetes (SearchProblem):
    def is_goal(self, state):
        return len(state[2]) == 5
    
    def cost(self, state, action, state2):
        if action[0] == "llevar":
            tiempo = 60/action[2]
            return tiempo
        else:
            return 3

    def actions(self, state):
        acciones=[]

        posicion_carro,deposito,ensamblado=state
        if posicion_carro == "deposito":
                if len(deposito) > 1 :
                    piezas_a_cargar = chain(combinations(deposito, 2))
                    for piezas in piezas_a_cargar:
                        pieza1, pieza2 = piezas
                        if pieza1[1]+pieza2[1] <= 8:
                            velocidad = min(pieza1[0],pieza2[0])
                            acciones.append(('llevar',piezas,velocidad,2))
                else:
                    pieza_a_cargar = deposito[0]
                    velocidad = pieza_a_cargar[0]
                    acciones.append(['llevar',pieza_a_cargar,velocidad,1])
        else:
            acciones.append('volver')

        return acciones

    
    def result(self, state, action):
        posicion, deposito, ensamblado = state
        depositolist = list(deposito)
        ensambladolist = list(ensamblado)
        if action[0] == 'llevar':
            if action[3]==2:
                pieza1,pieza2 = action[1]            
                depositolist.remove(pieza1)
                depositolist.remove(pieza2)
                ensambladolist.extend((pieza1,pieza2))
                nueva_pos = 'ensamblado'
            else:          
                depositolist.remove(action[1])
                ensambladolist.append(action[1])
                nueva_pos = 'ensamblado'
        else:
            nueva_pos = "deposito"
        
        newstate = (nueva_pos,tuple(depositolist),tuple(ensambladolist))

        return newstate    

    def heuristic(self, state):
        posicion, deposito, ensamblado = state
        estimacion = 0
        velocidades = []
        if posicion == "ensamblado":
            estimacion += 3
        if len(deposito) !=0:
            for velocidad,peso in deposito:
                velocidades.append(velocidad)          
            estimacion += min(velocidades)

        return estimacion


problem = ArmadoCohetes(INITIAL_STATE)

result = astar(problem)

METHODS = (
    breadth_first,
    greedy,
    astar
)    
        
for search_algorithm in METHODS:
    print()
    print('=' * 50)
    print("Running:", search_algorithm)
    visor = BaseViewer()
    problem =ArmadoCohetes(INITIAL_STATE)
    result = search_algorithm(problem, graph_search = True, viewer = visor)
    print ('Final State:', result.state)
    print('=' * 50)
    print(' - Statistics:')
    print(' - Amount of actions until goal:', len(result.path()))
    print(' - Raw data:', visor.stats)
    '''
    for action, state in result.path():
        print("   - Action:", action)
        print("   - Resulting State:", state)
    '''