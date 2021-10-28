from itertools import combinations
from simpleai.search import CspProblem, backtrack

ROBOTS = {
    'Alber':['ruedas'],
    'Bomber':['ruedas', 'paredes'],
    'Camina':['piernas','paredes'],
    'Destre':['piernas'],
    'Electro':['ruedas','paredes'],
    'Fire':['ruedas','paredes'],
    'Gun': ['piernas','paredes']

}

ROMPEDORES = ['Bomber','Camina','Electro', 'Paredes']

POSICIONES = ['posicion1','posicion2','posicion3','posicion4','posicion5','posicion6','posicion7']

problem_variables = POSICIONES


domains = {
    'posicion1':['Alber','Bomber','Destre','Fire','Gun','Electro'] ,
    'posicion2':['Alber','Bomber','Destre','Fire','Gun','Camina','Electro'] ,
    'posicion3':['Alber','Bomber','Destre','Fire','Gun','Camina','Electro'] ,
    'posicion4':['Alber','Bomber','Destre','Fire','Gun','Camina'] ,
    'posicion5':['Alber','Bomber','Destre','Fire','Gun','Camina'] ,
    'posicion6':['Alber','Bomber','Destre','Fire','Gun','Camina'] ,
    'posicion7':['Alber','Bomber','Destre','Fire','Gun','Camina' ] ,
}


constraints = []
#---------------------------------------------------------------------------------
def all_difs(varibles,values):
    robot1,robot2 = values
    return robot1!=robot2

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), all_difs)
    )
#--------------------------------------------------------------------------------
def alber_despues_de_rompedor(variables,values):
    variable1,variable2 = variables
    value1,value2 = values
    if value1 == 'Alber' and value2 == 'Bomber':
        return (POSICIONES.index(variable1) > POSICIONES.index(variable2))
    if value2 == 'Alber' and value1 == 'Bomber':
        return (POSICIONES.index(variable2) > POSICIONES.index(variable1))
    return True

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), alber_despues_de_rompedor)
    )
#--------------------------------------------------------------------------------
def bomber_despues_de_camimadores(variables,values):
    variable1,variable2 = variables
    value1,value2 = values
    if (value1 == 'Bomber' and 'piernas' in ROBOTS[value2]):
        return  (POSICIONES.index(variable1) > POSICIONES.index(variable2))
    if(value2 == 'Bomber' and 'piernas' in ROBOTS[value1]):
       return  (POSICIONES.index(variable2) > POSICIONES.index(variable1)) 
    return True

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), bomber_despues_de_camimadores)
    )
#--------------------------------------------------------------------------------
def destre_despues_de_rompedor(variables,values):
    variable1,variable2 = variables
    value1,value2 = values
    if value1 == 'Destre' and value2 == 'Electro':
        return(POSICIONES.index(variable1) > POSICIONES.index(variable2))
    if value2 == 'Destre' and value1 == 'Electro':
            return (POSICIONES.index(variable2) > POSICIONES.index(variable1))
    return True


for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), destre_despues_de_rompedor)
    )
#--------------------------------------------------------------------------------
def fire_despues_de_bomber(variables,values):
    variable1,variable2 = variables
    value1,value2 = values
    if (value1 == 'Fire' and value2 == 'Bomber'):
        return (POSICIONES.index(variable1)>POSICIONES.index(variable2))
    if (value2 == 'Fire' and value1 == 'Bomber'):
        return (POSICIONES.index(variable2)>POSICIONES.index(variable1))
    return True

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), fire_despues_de_bomber)
    )
#--------------------------------------------------------------------------------
def gun_antes_de_ruedas(variables,values):
    variable1,variable2 = variables
    value1,value2 = values
    if (value1 == 'Gun' and 'ruedas' in ROBOTS[value2]): 
        return (POSICIONES.index(variable1) < POSICIONES.index(variable2))
    return True

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2),  gun_antes_de_ruedas)
    )
#--------------------------------------------------------------------------------

problem = CspProblem(problem_variables, domains, constraints)
solution = backtrack(problem)

print("Solution:")
print(solution)


