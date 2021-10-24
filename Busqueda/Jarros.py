from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first
)

#cada jarro elemento es un numero de la tupla 
#y el numero indica la cantidad de agua
INITIAL_STATE = (0,0,0,4)

GOAL_STATE = (1,1,1,1)

class jarros(SearchProblem):

    def is_goal(self,state):
        return state == GOAL_STATE

    def cost (self):
        return 1

    def actions(self,state):
        actions = []
        # recorre los jarros y busca uno con agua
        for jarro_ori,agua_ori in enumerate(state): 
            if agua_ori != 0:
                for jarro_dest, agua_dest in enumerate(state):
                    if agua_dest < jarro_dest+1:
                        # pasa agua de un jarro a otro
                        agua_ori= agua_ori-1
                        agua_dest = agua_dest+1
                        #guarda el indice y la cantidad de agua con la que queda cada jarro
                        actions.append(((jarro_ori,agua_ori),(jarro_dest,agua_dest)))
        
        return actions

    def result(self,state,action):

        jarro_ori, agua_ori = action[0]
        jarro_dest,agua_dest = action[1]

        statelist = list(state)

        #pongo en el estado el agua que le corresponde a cada jarro 
        statelist[jarro_ori] = agua_ori
        statelist[jarro_dest] = agua_dest

        new_state = tuple(statelist)

        return new_state

problem = jarros(INITIAL_STATE)

result = breadth_first(problem, graph_search = True)

print(result)
print(result.path())
                



    
