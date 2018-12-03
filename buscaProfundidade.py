#Algoritmo responsável por fazer a busca em profundidade.

def bPf(grafo, inicio, destino, visitado=None):

    if visitado is None:
        visitado = set()

    visitado.add(inicio)

    if inicio == destino:
        return visitado

    for next in grafo[inicio] - visitado:
        bPf(grafo, next, visitado)
    return visitado
