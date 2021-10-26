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

INITIAL_STATE = ((0,2),(0,2)) #posiciones de los robot en el tablero

TABLERO =  [
    [0,0,1,0,'pos_def'],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,'pos_def',0,0]
]

class Robots_Defensivos(SearchProblem):

    def is_goal(self, state): #si la posicion de los robot NO es la misma y los dos estan en posiciones defensivas, devuelve true
        robot1, robot2 = state
        en_posicion = 0
        for fila in enumerate(TABLERO):
            for col,pos in enumerate(fila):
                if robot1!=robot2:
                    if robot1 == (fila,col) and pos == 'pos_def':
                        en_posicion+=1
                    if robot2 == (fila,col) and pos == 'pos_def':
                        en_posicion+=1
        
        return (True if en_posicion == 2 else False)

    def cost(self):
        return 1        

    def actions(self, state):
        aviable_actions = []
        robot1,robot2 = state
        
        fila_rb1,col_rb1 = robot1
        fila_rb2,col_rb2 = robot2
        
        if TABLERO[fila_rb1][col_rb1] != 'pos_def': #si no esta posiciones defesiva se mueve
            # the piece above
            if fila_rb1 > 0:
                if TABLERO[fila_rb1 - 1][col_rb1]!= 1: # antes pregunto si a donde se mueve no hay un obtaculo
                    aviable_actions.append((0, (fila_rb1 - 1,col_rb1)))
            # the piece below
            if fila_rb1 < 2:
                if TABLERO[fila_rb1 + 1][col_rb1]!= 1:
                    aviable_actions.append((0, (fila_rb1 + 1,col_rb1)))
            # the piece to the left
            if col_rb1 > 0:
                if TABLERO[fila_rb1][col_rb1 - 1] != 1:
                    aviable_actions.append((0, (fila_rb1, col_rb1 - 1)))
            # the piece to the right
            if col_rb1 < 2:
                if TABLERO[fila_rb1][col_rb1 + 1] != 1:
                    aviable_actions.append((0, (fila_rb1, col_rb1 + 1)))

        if TABLERO[fila_rb2][col_rb2] != 'pos_def':
            # the piece above
            if fila_rb2 > 0:
                if TABLERO[fila_rb2 - 1][col_rb2]!= 1:
                    aviable_actions.append((1, (fila_rb2 - 1,col_rb2)))
            # the piece below
            if fila_rb2 < 2:
                if TABLERO[fila_rb2 + 1][col_rb2]!= 1:
                    aviable_actions.append((1, (fila_rb2 + 1,col_rb2)))
            # the piece to the left
            if col_rb2 > 0:
                if TABLERO[fila_rb2][col_rb2 - 1] != 1:
                    aviable_actions.append((1, (fila_rb2, col_rb2 - 1)))
            # the piece to the right
            if col_rb2 < 2:
                if TABLERO[fila_rb2][col_rb2 + 1] != 1:
                    aviable_actions.append((1, (fila_rb2, col_rb2 + 1)))  
            
        return aviable_actions

    def result(self, state, action):
        
        robot, nueva_pos = action
        newstate = list(state)
        newstate[robot]= nueva_pos;

        return tuple(newstate);

        
problem = Robots_Defensivos(INITIAL_STATE)

result = astar(problem)

METHODS = (
    breadth_first,
    depth_first,
    uniform_cost,
    greedy,
    astar
)    
        
for search_algorithm in METHODS:
    print()
    print('=' * 50)
    print("Running:", search_algorithm)
    visor = BaseViewer()
    problem =Robots_Defensivos(INITIAL_STATE)
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