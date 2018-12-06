import networkx as nx
import matplotlib.pyplot as plt


def getGrafo():
    cidades = open('./arquivos/distancias.csv')

    grafo = nx.Graph()

    for linha in cidades:
        data = linha.split(",")
        data[2] = data[2].replace("\n", "")
        grafo.add_edge(data[0], data[1], weight=float(data[2]))

    return grafo

def getDistanciaTotal():
    distCidades = open('./arquivos/distanciasTotais.csv')
    matrizDist = []

    for linha in distCidades:
        data = linha.split(",")
        data[len(data) - 1] = data[len(data) - 1].replace("\n", "")
        data.remove(data[0])
        matrizDist.append(data)

    ordemCidades = matrizDist[0]
    matrizDist.remove(matrizDist[0])

    for i in range(len(matrizDist)):
        for j in range(len(matrizDist[i])):
            if j >= i:
                matrizDist[i][j] = float(matrizDist[i][j])
            else:
                matrizDist[i][j] = None

    return ordemCidades, matrizDist

def showGrafo(grafo):
    plt.figure(1, figsize=(12, 8))             #definindo o tamanho da figura
    pos=nx.fruchterman_reingold_layout(grafo)      #definindo o algoritmo do layout
    plt.axis('off')                            #retira as bordas
    nx.draw_networkx_nodes(grafo,pos,node_size=1000) #plota os nos
    nx.draw_networkx_edges(grafo,pos,alpha=0.8)    #plota as arestas
    plt.title('Cidades', size=16)     #Título
    plt.show()