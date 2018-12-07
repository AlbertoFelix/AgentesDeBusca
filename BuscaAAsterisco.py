def getDistancia(cidade1, cidade2, ordemCidades, matrizDist):
    c1 = None
    c2 = None
    for i in range(len(ordemCidades)):
        if cidade1 == ordemCidades[i]:
            c1 = i
        if cidade2 == ordemCidades[i]:
            c2 = i

    if matrizDist[c1][c2] is None:
        return matrizDist[c2][c1]
    else:
        return matrizDist[c1][c2]


def heuristica(grafo, inicio, destino, ordemCidades, matrizDist, visitado):
    min = 100000000000
    city = None
    for cidade in grafo[inicio]:
        if (min == None) and (cidade not in visitado):
            min = grafo[inicio][cidade]['weight'] + getDistancia(cidade, destino, ordemCidades, matrizDist) #F(n) = G(n) + H(n)
            city = cidade
        else:
            if (grafo[inicio][cidade]['weight'] + getDistancia(cidade, destino, ordemCidades, matrizDist) < min) and (cidade not in visitado):
                min = grafo[inicio][cidade]['weight'] + getDistancia(cidade, destino, ordemCidades, matrizDist) #F(n) = G(n) + H(n)
                city = cidade
    return city

def aAsterisco(grafo, ordemCidades, matrizDist, inicio, destino, visitado=None):
    if visitado is None:
        visitado = [inicio]

    if inicio == destino:
        return visitado

    proximo = heuristica(grafo, inicio, destino, ordemCidades, matrizDist, visitado)

    return aAsterisco(grafo, ordemCidades, matrizDist, proximo, destino, visitado + [proximo])