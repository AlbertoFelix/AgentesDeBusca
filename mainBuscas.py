#Iniciando Projeto de Agentes de Buscas

'''Buscas a serem implementadas:
	Busca em Largura
	Busca em Profundidade
	Busca A* com Heurística
'''
from Grafo import *
from buscaProfundidade import *
from BuscaEmLargura import *
from BuscaAAsterisco import *

grafo = getGrafo()

ordemCidades, matrizDist = getDistanciaTotal()
grafo = getGrafo()
showGrafo(grafo)
print(aAsterisco(grafo, ordemCidades, matrizDist, 'Arad', 'Neamt'))
print(busca_largura(grafo, 'Arad', 'Bucharest'))
print(busca_largura_melhorCaminho(grafo, 'Arad', 'Bucharest'))