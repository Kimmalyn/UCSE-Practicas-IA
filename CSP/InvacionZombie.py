from datetime import datetime
from itertools import combinations
from operator import truediv

from simpleai.search import MOST_CONSTRAINED_VARIABLE, CspProblem, backtrack

GRILLA = [(f,c) for f in range(5) for c in range(6)]

ESQUINAS = [(0,0),(0,4),(4,0),(4,4)]

ELEMENTOS = ['zombie', 'zombie', 'zombie', 'zombie', 'zombie', 
            'pared', 'pared', 'pared', 'pared', 'pared', 'pared', 'pared']

problem_variables = ELEMENTOS

domains={}

domains['protagonista'] = ESQUINAS
domains['zonasegura'] = ESQUINAS

for celda in ESQUINAS:
    GRILLA.remove(celda)

for item in problem_variables:
    domains[item] = GRILLA

constraints=[]

def son_adyacentes(variables):
    "dada una tupla de dos variables devuelve si las mismas son adyacentes"
    v1, v2 = variables
    distancia = abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
    return distancia == 1

def adyacentes_de(variable):
    "Dada una variable, devuelve todas las variables adyacentes a la misma"
    adyacentes = []
    fila, columna = variable
    for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nf = fila + df
        nc = columna + dc
        if 0 <= nf <= 4 and 0 <= nc <= 4:
            adyacentes.append((nf, nc))
    return adyacentes

def all_dif(variables,values):
    value1,value2 = values

    return value1!=value2

def no_mas_2_zombies_adyacentes(variables,values):

    if "zombies" in variables:
        adyacentes = adyacentes_de(variables)
        if len(adyacentes) >= 2:
            return True
        
    return False

def jugador_y_zonasegura_esquina_distintas(variables,values):
    value1,value2 = values
    if (value1 == (0,0) and value2 == (4,4)) or (value1 == (0,4) and value2 == (4,0)):
        return True
    if (value1 == (4,4) and value2 == (0,0)) or (value1 == (4,0) and value2 == (0,4)):
        return True
    
    return False

def pared_en_zonasegura(variables,values):
    if "zonasegura" in variables:
        adyacentes = adyacentes_de(variables)
        if len(adyacentes) >=1:
            return True
        
    return False   


    



