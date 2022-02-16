from datetime import datetime
from itertools import combinations
from simpleai.search import MOST_CONSTRAINED_VARIABLE, CspProblem, backtrack

PERIODISTAS = ['cnn1','cnn2', 'fox', 'bbc', 'the onion', 'msnbc1', 'msnbc2', 'msnbc3', 'rt', 'infobae1','infobae2']

LUGARESDISPONIBLES = [
(1,0),(1,1),(1,2),(1,3),
(2,0),(2,1),(2,2),(2,3),]

domains={}

#Estos van en primera fila si o si
domains['cnn1'] = [(0,0),(0,1),(0,2),(0,3)]
domains['cnn2'] = [(0,0),(0,1),(0,2),(0,3)]
domains['fox'] = [(0,0),(0,1),(0,2),(0,3)]
domains['bbc'] = [(0,0),(0,1),(0,2),(0,3)]
#the onion en la ultima fila
domains['the onion'] = [(2,0),(2,1),(2,2),(2,3)]
domains['msnbc1'] = LUGARESDISPONIBLES
domains['msnbc2'] = LUGARESDISPONIBLES
domains['msnbc3'] = LUGARESDISPONIBLES
domains['rt'] = LUGARESDISPONIBLES
domains['infobae1'] = LUGARESDISPONIBLES
domains['infobae2'] = LUGARESDISPONIBLES

constraints = []

def cnn_contiguos(variables, values):
    cnn1,cnn2 = vvalues

    if cnn2[1] == cnn1[1]+1 or cnn2[1] == cnn1[1]-1:
        return True
    
    return False

constraints.append((('cnn1','cnn2'),cnn_contiguos))

def bbc_y_fox_separados(variables, values):
    bbc,fox = values
  
    if bbc[1] == fox[1]+1 or bbc[1] == fox[1]-1:
        return False

    return True

constraints.append((('bbc','fox'),cnn_contiguos))

def msnbc_contiguos(variables,values):
    msnbc1, msnbc2, msnbc3 = values

    if msnbc1[0] == msnbc2[0] and msnbc2[0] == msnbc3[0]:
        if msnbc1[1] == msnbc2[1]+1 and msnbc2[1] == msnbc3[1]+1:
            return True
    
    return False

constraints.append((('msnbc1','msnbc2','msnbc3'), msnbc_contiguos))









