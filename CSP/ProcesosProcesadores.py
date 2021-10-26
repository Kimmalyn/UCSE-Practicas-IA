from itertools import combinations
from simpleai.search import CspProblem, backtrack

SERVIDORES = {
    'Tesla':(8,32),
    'Goedel':(4,16),
    'Bohr':(4,16)
}

TAREAS = {
    'Limpiador de Datos': (2,10),
    'Convertidor de Entradas':(5,20),
    'Entrenador de Modelos': (5, 14),
    'Almacenador de Estadisticas': (1, 1),
    'Graficador de Resultados': (2,2),
    'Serivdor API':(2,8)
}