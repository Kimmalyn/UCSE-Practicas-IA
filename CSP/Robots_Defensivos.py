from itertools import combinations
from simpleai.search import CspProblem, backtrack

ROBOTS = ["robot1","robot2","robot3","robot4","robot5","robot6"]

columns = list(range(5))
rows = list(range(4))

HABITACIONES = [
    (row, col)
    for row in rows
    for col in columns
]

PROHIBIDAS = [(0,2),(1,3),(2,1)] # habitaciones por las que los robot no pueden pasar

for habitacion in PROHIBIDAS: # saco las prohibidas de la lista de habitaciones porque no son posiciones validas en el dominio
    HABITACIONES.remove(habitacion)

problem_variables = ROBOTS

domains = {}

#asigno las posiciones fijas al los dos primeros robots y las saco de las habitaciones restantes
domains["robot1"]=[(0,4)]
HABITACIONES.remove((0,4))

domains["robot2"]=[(3,2)]
HABITACIONES.remove((3,2))

for robot in problem_variables: 
    #asigno las que quedan al resto de robots
    if robot!= "robot1" and robot!= "robot2":
        domains[robot] = HABITACIONES

print("Variables:", ROBOTS)
print("Domains:", domains)

constraints = []

def habitaciones_diferentes(variables, values): 
    #all dif para que ninguno este en la misma posicion
    robot1, robot2 = values
    return robot1 != robot2


for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), habitaciones_diferentes)
    )

def habitaciones_no_adyacentes(variables,values): 
    #comparo de a 2 robots para verificar que no esten adyacentes entre ellos
    #preguntando si en las adyacentes del primer robot se encuentra el segundo
    
    robot1,robot2 = values

    return (robot2 != (robot1[0]-1,robot1[1]) 
        and robot2 != (robot1[0]+1,robot1[1])
        and robot2 != (robot1[0],robot1[1]-1)
        and robot2 != (robot1[0],robot1[1]+1))    

for robot1, robot2 in combinations(problem_variables, 2):
    constraints.append(
        ((robot1, robot2), habitaciones_no_adyacentes)
    ) 

problem = CspProblem(problem_variables, domains, constraints)
solution = backtrack(problem)

print("Solution:")
print(solution)