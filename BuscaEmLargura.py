def busca_largura(graph, start, goal):

    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set([i for i in graph.neighbors(vertex)]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
