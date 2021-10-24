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

def planear_escaneo (tuneles,robots):
    pass

#(posicion bombero, habitaciones : cantidad de segundos para apagar fuego)
INITIAL_STATE = ("entrada",({"entrada":0,"living":10,"dormitorio":10,"comedor":600,"baño":30}))

HABITACIONES = {
                "entrada": ["living"],
                "living": ["entrada","dormitorio","comedor"],
                "dormitorio":["living"],
                "comedor":["living", "baño"],
                "baño": ["comedor"]
               }

GOAL_STATE = ()

class Bomberos(SearchProblem):

    def cost(self, state, action, state2):
        #si es "ir" devuelvo 5 sino los segundos que se demora en apagar
        tipo, parametro = action
        if tipo == "ir":
            return 5
        else:
            return parametro
        
    
    def is_goal(self, state):
        bomberos,fuegos_restantes = state
        #si hay alguno que tiene fuego devuelve false
        for habitacion,fuegos_restantes in fuegos_restantes.items():
            if fuegos_restantes != 0:
                 return False
        #si no freno es que todos estan apagados devuelve true
        return True

    def actions(self, state):
        # las acciones son (ir, "habitacion") o (rociar, "segundos")
        actions = []

        bombero, fuegos_restantes = state

        #si hay fuego se agrega rociar
        if fuegos_restantes[bombero] != 0:
            actions.append(("rociar",fuegos_restantes[bombero]))
        
        #agregamos una accion de moverse por cada habitacion accesible desde donde esta el bombero
        for habitacion_accesible in HABITACIONES[bombero]:
            actions.append(("ir", habitacion_accesible))
            
        return actions
    
    def result(self, state, action):
        # pregunto si la accion es ir o rociar y cambio el estado segun corresponda apagar o moverse
        bombero,fuegos_restantes = state
        tipo, parametro = action
        if tipo == "ir":
            bombero = parametro
        else:
            fuegos_restantes[bombero]= 0
        
        return(bombero,(fuegos_restantes))
    
    def heuristic(self, state):
        # estimamos que como mínimo nos falta este tiempo:
        # - la duración de todos los fuegos activos sumados
        # - 5 segundos por cada habitación con fuego que no sea la actual
        estimacion = 0
        habitacion_bombero, fuegos_restantes = state

        for habitacion, fuego_restante in fuegos_restantes.items():
            estimacion += fuego_restante

            if habitacion != habitacion_bombero and fuego_restante > 0:
                estimacion += 5

        return estimacion

problem = Bomberos(INITIAL_STATE)

result = astar(problem)

print(result)
print(result.path())


