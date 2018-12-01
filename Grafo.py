import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

cidades = open('./arquivos/distancias.csv')

grafo = nx.Graph()

for linha in cidades:
    data = linha.split(",")
    data[2] = data[2].replace("\n", "")
    grafo.add_edge(data[0], data[1], weight=float(data[2]))


plt.figure(1, figsize=(12, 8))             #definindo o tamanho da figura
pos=nx.fruchterman_reingold_layout(grafo)      #definindo o algoritmo do layout
plt.axis('off')                            #retira as bordas
nx.draw_networkx_nodes(grafo,pos,node_size=1000) #plota os nos
nx.draw_networkx_edges(grafo,pos,alpha=0.8)    #plota as arestas
plt.title('Cidades', size=16)     #Título
plt.show()