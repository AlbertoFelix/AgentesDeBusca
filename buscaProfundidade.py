def bPf(grafo, inicio, destino, visitado=None):

    if visitado is None:
        visitado = [inicio]

    if inicio == destino:
        return visitado

    for next in (grafo[inicio]):
        if(next not in visitado):
            print(next)
            return bPf(grafo, next, destino, visitado + [next])