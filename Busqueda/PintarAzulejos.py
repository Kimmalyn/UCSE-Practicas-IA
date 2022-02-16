from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)

WALL = ((r,c) for r in range(5) for c in range(5))

INITIAL_STATE = WALL

class Azulejos(SearchProblem):

    def adjacent(grid):
        adjacents = []
        arriba = grid[0],grid[1]+1
        abajo = grid[0],grid[1]-1
        derecha = grid[0]+1,grid[1]
        izquierda = grid[0]-1,grid[1]
        adjacents.extend([arriba,abajo,derecha,izquierda])

    
    def is_goal(self, state):
        return len(state)==0

    def cost(self, state, action, state2):
        return 1
    
    def actions(self, state):
        actions=[]
        for celda in state:
            actions.append(celda)
            adyacentes=adjacent(celda)
            for celda_ady in adyacentes:
                if celda_ady in state:
                    actions.append(celda_ady)

  
    def result(self, state, action):
        state_list = list(state)
        for celda in action:
            state_list.remove(celda);
        
        return tuple(state)


    def heuristic(self, state):
        return len(list(WALL))/5


problem = Azulejos(INITIAL_STATE)

result = astar(problem)

print(result)
print(result.path())