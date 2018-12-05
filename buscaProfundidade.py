def busca_profundidade(grafo, inicio, destino, visitados=None):

    if visitados is None:
        visitados = [inicio]

    if inicio == destino:
        return visitados

    for proximo in grafo[inicio]:

        if proximo not in visitados and destino not in visitados:
            visitados = busca_profundidade(grafo, proximo, destino, visitados + [proximo])

    return visitados
