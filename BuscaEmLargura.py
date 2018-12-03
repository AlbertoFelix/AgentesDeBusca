from Grafo import grafo


def busca_largura(graph, start, goal):
    """Algoritmo de busca em largura
        Retorna um generator contendo todos os caminhos encontados na busca"""
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set([i for i in graph.neighbors(vertex)]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

v = next(busca_largura(grafo,'Arad','Dobretu'))
print(v)