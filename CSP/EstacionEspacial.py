from itertools import combinations
from simpleai.search import CspProblem, backtrack

SLOSTS = ['slost1', 'slost2', 'slost3'] #variables

MEJORAS = { #dominios
    'Baterias': (12.5,300),
    'Brazo Robotico': (60,50),
    'Observacion Espacial': (100,550),
    'Antena de Comunicaciones':(20,30),
    'Laboratorios de Plantas':(80,250),
    'Laboratorios de Fisicos':(75,300),
    'Computadoras de Control':(50,20),
    'Reciclador de Oxigeno':(30,100)
}

problem_variables = SLOSTS

domains={}

for slot in problem_variables:
    domains[slot]=[
        'Baterias',
        'Brazo Robotico',
        'Observacion Espacial',
        'Antena de Comunicaciones',
        'Laboratorios de Plantas',
        'Laboratorios de Fisicos',
        'Computadoras de Control',
        'Reciclador de Oxigeno',
    ]

print (domains)

constraints=[]

def distintos (variables,values):
    mejora1, mejora2 = values
    return mejora1!=mejora2

for mejora1, mejora2 in combinations(problem_variables, 2):
    constraints.append(
        ((mejora1, mejora2), distintos)
    )
    
def limite_presupuesto(variables,values):
    mejora1,mejora2,mejora3 = values
    return (MEJORAS[mejora1][0]+MEJORAS[mejora2][0]+MEJORAS[mejora3][0])<=150

for mejora1, mejora2, mejora3 in combinations(problem_variables, 3):
    constraints.append(
        ((mejora1, mejora2, mejora3), limite_presupuesto)
    )

def limite_peso(variables,values):
    mejora1,mejora2,mejora3 = values
    return (MEJORAS[mejora1][1]+MEJORAS[mejora2][1]+MEJORAS[mejora3][1])<=1000

for mejora1, mejora2, mejora3 in combinations(problem_variables, 3):
    constraints.append(
        ((mejora1, mejora2, mejora3), limite_peso)
    )

problem = CspProblem(problem_variables, domains, constraints)
solution = backtrack(problem)

print("Solution:")
print(solution)
