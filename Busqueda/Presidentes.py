from simpleai.search import (
    SearchProblem, 
    breadth_first, 
    depth_first, 
    uniform_cost,
    limited_depth_first,
    iterative_limited_depth_first,
    astar
)

#cada tupla es una habitacion y dentro tiene los presdentes representados por su orientacion politica
INITIAL_STATE = (("cap","cap","com","com","cen","cen"),(),())

# estado meta (no importa el orden) es: [(),(),("cap","cap","com","com","cen","cen")]

class Presidentes(SearchProblem):

    def is_goal(self, state):
        #cuenta la cantidad de presidentes en la tercer sala si es 6 el estado, es meta, todos los presidentes pasaron
        cont=0
        for presidentes in state[2]:
            cont+=1
        return cont == 6
    
    def cost(self):
        #cada movimiento de habitacion cuesta lo mismo
        return 1

    def actions(self, state):
        actions = []

        #Recorro el estado buscando las habitaciones y preguntando siempre que no sea la 3.
        #Luego pregunto si tiene dos o mas presidentes. En ese caso me aseguro que la accion sea valida preguntando si los presindentes que voy a pasar no son iguales
        #y si no tienen un anterior adyacente del mismo tipo luego agrego los dos presidentes y el indice de la habitacion siguente
        #en caso de sea 1 hago las misma validaciones pero solo agrego un presidente y la habitacion que voy a pasar

        for num_hab,habitacion in enumerate(state):
                habitacion_sig = list(state[num_hab+1])
                habitacion_ant = list(state[num_hab-1])

                if num_hab != 3:
                    if len(habitacion)>=2:
                        for presidente in habitacion:
                            igual = 0

                            for presidente_ant in habitacion_ant:
                                if presidente_ant == habitacion[0]:
                                    igual = 1
                                if presidente_ant == presidente:
                                    igual = 1

                            if habitacion[0]!=presidente and igual == 0:                                
                                    actions.append((habitacion[0],presidente, num_hab+1))
                    else:
                        igual = 0

                        for presidente in habitacion_sig:
                            if presidente == habitacion[0] and habitacion_ant.count() == 1:
                                igual = 1

                        for presidente in habitacion_ant:
                            if presidente == habitacion[0]:
                                igual = 1

                        if igual != 1: 
                            actions.append((habitacion[0], num_hab +1))
                        
        return actions;
    
    def result(self, state, action):
        #desarmo la tupla dependiente de si es 1 o 2 presidentes y armo el nuevo estado con la accion correspondiente

        statelist=list(state)
        if action.count() == 3:
            presidente1, presidente2, habitacion = action
            
            statelist[habitacion].append(presidente1,presidente2);

            statelist[habitacion-1].remove(presidente1,presidente2);
        else:
            presidente, habitacion = action

            statelist[habitacion].append(presidente);

            statelist[habitacion-1].remove(presidente);
        
        statetuple=tuple(statelist)

        return statetuple

    def heuristic(self, state):
        return super().heuristic(state)

problem = Presidentes(INITIAL_STATE)

result = breadth_first(problem, graph_search = True)

print(result)
print(result.path())
                