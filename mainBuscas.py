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
from termcolor import colored

def print_caminho(caminho):
    for i in range(len(caminho)):
        if i == 0:
            print(colored(str(i + 1) + '- ' + caminho[i], 'red'))
        elif i == len(caminho) - 1:
            print(colored(str(i + 1) + '- ' + caminho[i], 'cyan'))
        else:
            print(colored(str(i + 1) + '- ' + caminho[i], 'yellow'))

ordemCidades, matrizDist = getDistanciaTotal()
grafo = getGrafo()

while True:
    inicio = input("Origem: \n")
    if inicio not in grafo.nodes:
        print("{} não contida na KB".format(inicio))
        continue
    destino = input("Destino: \n")
    if destino not in grafo.nodes:
        print("{} não contida na KB".format(destino))
        continue
    alg = int(
        input("Qual algorítmo usar?\n1 - Busca em largura\n2 - Busca em largura melhor caminho\n3 - Busca em Profundidade\n4 - A*\n"))
    if alg == 1:
        print("Busca em largura\n{} para {}".format(inicio, destino))
        caminho = busca_largura(grafo, inicio, destino)
        print_caminho(caminho)

    elif alg == 2:
        print("Busca em largura melhor caminho\n{} para {}".format(inicio, destino))
        caminho = busca_largura_melhorCaminho(grafo, inicio, destino)
        print_caminho(caminho)
    elif alg == 3:
        print("Busca em profundidade\n{} para {}".format(inicio, destino))
        caminho = busca_profundidade(grafo, inicio, destino)
        print_caminho(caminho)
    elif alg == 4:
        print("Busca em A*\n{} para {}".format(inicio, destino))
        caminho = aAsterisco(grafo, ordemCidades, matrizDist, inicio, destino)
        print_caminho(caminho)
    else:
        break
