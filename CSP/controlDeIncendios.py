from datetime import datetime
from itertools import combinations
from simpleai.search import MOST_CONSTRAINED_VARIABLE, CspProblem, backtrack

ESTACIONES = ['A','B','C']

ADYACENTES = {
    '42 de julio':['ciclovialandia','centro','barrio estandar 2'],
    'ciclovialandia':['quintas','42 de julio','centro'],
    'quintas':['ciclovialandia'],
    'parque industrial':['barrio estandar 1', 'barrio estandar 2' ],
    'barrio estandar 2':['42 de julio', 'centro', 'barrio estandar 1'],
    'barrio estandar 1':['centro', 'barrio estandar 2', 'barrio estandar 3', 'costanera', 'parque industrial'],
    'aeroclub':['centro','costanera'],
    'costanera':['aeroclub', 'centro', 'barrio estandar 1'],
    'barrio estandar 3':['barrio estandar 1', 'parque industrial', 'costanera']
}

#'centro':['ciclovialandia', '42 de julio', 'barrio estandar 1', 'barrio estandar 2','aeroclub','costanera'],
BARRIOS = ['42 de julio', 'ciclovialandia', 'quintas', 'barrio estandar 2', 'barrio estandar 1', 'aeroclub', 'costanera', 'barrio estandar 3', 'parque industrial' ]

problem_variables = ESTACIONES

domains={}

domains['A'] = ['42 de julio', 'ciclovialandia', 'barrio estandar 2', 'barrio estandar 1', 'aeroclub', 'costanera'] #los adyacentes de centro

domains['B'] = ['42 de julio', 'ciclovialandia', 'barrio estandar 2', 'barrio estandar 1', 'costanera', 'barrio estandar 3']# todos menos quintas parque industrial y aeroclub

domains['C'] = BARRIOS

constraints = []

def all_dif(variables,values):
    barrio1,barrio2,barrio3 = values

    return (barrio1!=barrio2 and barrio1!=barrio3 and barrio2!=barrio3)

constraints.append(all_dif)

def no_adyacentes(variables, values):
    






