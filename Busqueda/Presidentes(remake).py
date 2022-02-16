from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)
import itertools

#cada tupla es una habitacion y dentro tiene los presdentes representados por su orientacion politica
INITIAL_STATE = (("cap","cap","com","com","cen","cen"),(),())

# estado meta (no importa el orden) es: [(),(),("cap","cap","com","com","cen","cen")]

class Presidentes(SearchProblem):

    def is_goal(self, state):
        return len(state[2]) == 6

    def cost(self, state, action, state2):
        return 1
    
    def actions(self, state):
        acciones = []
        sala1,sala2,sala3 = state
        for index,sala in state:
            if len(sala >= 2):
                for presi1,presi2 in combinations(sala):                       
                    if len(sala[index+1]) > 1:
                        if presi1 in sala[index+1]:
                            if presi1!=presi2:
                                acciones((presi1,presi2), index+1)
                        else:
                            acciones
                        


    def result(self, state, action):
        pass