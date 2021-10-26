
from itertools import chain, combinations
izquierda = (10,30,60,80,120)
grupos = chain(combinations(izquierda, 2))
for grupo in grupos:
    print (grupo)
