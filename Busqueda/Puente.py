from itertools import chain, combinations
from simpleai.search import (
    SearchProblem, 
    breadth_first,
    greedy, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer

INITIAL_STATE = ((10,30,60,80,120),(),(0,300))

class Puente (SearchProblem):

    def is_goal(self, state):
        _,_,linterna = state
        return ((len(state[1])==5))
    
    def cost(self, state, action, state2):
        if len(action)==3:
            persona1,persona2,_ = action
            return max(persona1,persona2)
        else:
            persona,_ = action
            return persona
    
    def actions(self, state):
        actions= []

        izquierda, derecha, linterna = state

        lado, bateria = linterna

        if len(izquierda) != 0 and bateria != 0: # si hay personas para pasar y hay bateria
            if lado == 0:
                if len(izquierda)>1: 
                    #si hay mas de una persona a la izquierda hago combinaciones de dos
                    #pregunto si el mayor en la combinacion es igual o menor a la bateria para pasarlo
                    grupos = chain(combinations(izquierda, 2))
                    for grupo in grupos:
                        persona1,persona2 = grupo
                        if max(grupo)<= bateria:
                            actions.append((persona1, persona2, lado))
                else:
                    #si queda solo uno solo paso ese
                    if izquierda[0] <= bateria:  
                        actions.append((izquierda[0], lado))   
            else:
                #vuelve la persona que menos bateria gasta de todos
                persona = min(derecha)
                if persona <= bateria:
                    actions.append((persona,lado))

        return actions

    
    def result(self, state, action):
        izquierda,derecha,linterna = state
        izquierdalist = list(izquierda)
        derechalist = list(derecha)
        linternalist = list(linterna)
        new_state=[]
        if len(action) == 3:
            persona1,persona2,lado = action
            if lado == 0:
                izquierdalist.remove(persona1)
                izquierdalist.remove(persona2)
                derechalist.append(persona1)
                derechalist.append(persona2)
                linternalist[0] = 1
                linternalist[1] = linternalist[1]-max((persona1,persona2))
            else:
                derechalist.remove(persona1)
                derechalist.remove(persona2)
                izquierdalist.append(persona1)
                izquierdalist.append(persona2)
                linternalist[0] = 0
                linternalist[1] = linternalist[1]-max((persona1,persona2))
        else:
            persona,lado = action
                    
            if lado == 0:
                izquierdalist.remove(persona)
                derechalist.append(persona)
                linterna[0] = 1
                linterna[1] = linterna[1]-persona
            else:
                derechalist.remove(persona)
                izquierdalist.append(persona)
                linternalist[0] = 0
                linternalist[1] = linterna[1]-persona

        new_state.extend((tuple(izquierdalist),tuple(derechalist),tuple(linternalist)))
        return tuple(new_state)

    def heuristic(self, state):
        if len(state[0])>1:
            return min(state[0])

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
    problem = Puente(INITIAL_STATE)
    result = search_algorithm(problem, graph_search = True)
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



