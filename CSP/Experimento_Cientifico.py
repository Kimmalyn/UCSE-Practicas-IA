from itertools import combinations
from simpleai.search import CspProblem, backtrack


PROCESOS = ['S','I','M','R','G','D','C','E'] #variables

POSICIONES = [1,2,3,4,5,6,7,8] #dominios

problem_variables = PROCESOS

domains={
    'S':[2,3,4,5,6,7,8],
    'I':[2,3,4,5,6,7,8],
    'M':[1],
    'R':[2,3,4,5,6,7,8],
    'G':[2,3,4,5,6,7,8],
    'G':[2,3,4,5,6,7,8],
    'D':[2,3,4,5,6,7,8],
    'C':[2,3,4,5,6,7,8],
    'E':[2,3,4,5,6,7,8],
}

constraints=[]

def all_difs(variables,values):
    value1,value2 = values
    return value1!=value2

for value1,value2 in combinations(problem_variables, 2):
    constraints.append(
        ((value1,value2), all_difs)
    )

def Inhibidor_Despues_3(variables,values):
    value1 = values[0]
    return value1 > 3
constraints.append(('I', Inhibidor_Despues_3))

def Despues_Antes_Que(variables,values):
    value1,value2 = values
    return value1<value2

#Regulador antes que Sopaperizador
constraints.append((('R','S'), Despues_Antes_Que))
#Generador de despues de Sopaperizador
constraints.append((('S','G'), Despues_Antes_Que))
#Derretidor antes de Generador despues de Sopaperizador
constraints.append((('D','G'), Despues_Antes_Que))
constraints.append((('S','D'), Despues_Antes_Que))
#Compilador despues de derretidor y generador
constraints.append((('D','C'), Despues_Antes_Que))
constraints.append((('G','C'), Despues_Antes_Que))
#Explotador antes de Regulador e Inhibidor
constraints.append((('E','R'), Despues_Antes_Que))
constraints.append((('E','I'), Despues_Antes_Que))

problem = CspProblem(problem_variables, domains, constraints)
solution = backtrack(problem)

print("Solution:")
print(solution)