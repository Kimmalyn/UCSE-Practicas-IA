from itertools import combinations
from simpleai.search import CspProblem, backtrack

OBJECTS = {
    'Assault Cuirass':5000,
    'Battlefury':4000,
    'Cloak':500,
    'Hyperstone':2000,
    'Quelling Blade':200,
    'Shadow Blade':3000,
    'Veil of Discord':2000
    }

INVENTORY = ['item1', 'item2', 'item3']

problem_variables = INVENTORY

domains = {}

for item in problem_variables:
    domains[item] = [
        'Assault Cuirass',
        'Battlefury',
        'Cloak',
        'Hyperstone',
        'Quelling Blade',
        'Shadow Blade',
        'Veil of Discord',
    ]

print(domains)

constraints = []

def menos_de_seismil(variables,values):
    object1, object2, object3 = values
    return (OBJECTS[object1]+OBJECTS[object2]+OBJECTS[object3])<=6000

for object1, object2, object3 in combinations(problem_variables, 3):
    constraints.append(
        ((object1, object2, object3), menos_de_seismil)
    )

def hyper_o_shadow(variables,values):
    item1, item2 = values
    if item1 == 'Hyperstone' and item2 == 'Shadow Blade':
        return False
    return True
    
for item1, item2 in combinations(problem_variables, 2):
    constraints.append(
        ((item1, item2), hyper_o_shadow)
    )

def quelling_o_shadow(variables,values):
    item1, item2 = values
    if item1 == 'Quelling Blade' and item2 == 'Shadow Blade':
        return False
    return True

for item1, item2 in combinations(problem_variables, 2):
    constraints.append(
        ((item1, item2), hyper_o_shadow)
    )

def cloak_o_veil(variables,values):
    item1, item2 = values
    if item1 == 'Cloak' and item2 == 'Veil of Discord':
        return False
    return True

for item1, item2 in combinations(problem_variables, 2):
    constraints.append(
        ((item1, item2), cloak_o_veil)
    )

def regeneradores(variables,values):
    object1, object2 = values
    if ('Cloak' in values and 'Veil of discord' in values):
        return False
    return True

for object1, object2 in combinations(problem_variables, 2):
    constraints.append(
        ((object1, object2), regeneradores)
    )

def distintos(varibles,values):
    object1,object2 = values
    return object1!=object2

for object1, object2 in combinations(problem_variables, 2):
    constraints.append(
        ((object1, object2), distintos)
    )

problem = CspProblem(problem_variables, domains, constraints)
solution = backtrack(problem)

print("Solution:")
print(solution)