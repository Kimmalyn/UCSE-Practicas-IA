from abc import abstractproperty
from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)

INITIAL_STATE = ("Deposito", ((10,7),(15,3),(20,1),(5,0.5),(5,1.5)),())

class ArmadoCohetes (SearchProblem):
    def is_goal(self, state):
        return super().is_goal(state)
    
    def cost(self, state, action, state2):
        return super().cost(state, action, state2)

    def actions(self, state):
        return super().actions(state)
    
    def result(self, state, action):
        return super().result(state, action)