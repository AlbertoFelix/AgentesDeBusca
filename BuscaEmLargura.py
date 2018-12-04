def busca_largura(graph, start, goal):

    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set([i for i in graph.neighbors(vertex)]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def busca_largura_not_recursive(grafo, inicio, destino):
    visitado = []

    fila = [inicio]

    while fila:

        cidade = fila.pop(0)

        if cidade not in visitado:
            visitado.append(cidade)
            proximos = grafo[cidade]

            for proximo in proximos:
                fila.append(proximo)
        if cidade == destino:
            return visitado