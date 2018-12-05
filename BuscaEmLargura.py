def busca_largura(grafo, inicio, destino):

    visitado = []

    fila = [inicio]

    if inicio == destino:
        return [inicio]

    while fila:

        cidade = fila.pop(0)

        if cidade not in visitado:
            visitado.append(cidade)
            proximos = grafo[cidade]

            for proximo in proximos:
                fila.append(proximo)
        if cidade == destino:
            return visitado
    return "Não existe um Caminho"


def busca_largura_melhorCaminho(grafo, inicio, destino):

    visitado = []

    fila = [[inicio]]


    if inicio == destino:
        return [inicio]


    while fila:

        caminho = fila.pop(0)

        cidade = caminho[-1]

        if cidade not in visitado:

            visinhos = grafo[cidade]

            for visinho in visinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(visinho)
                fila.append(novo_caminho)

                if visinho == destino:
                    return novo_caminho


            visitado.append(cidade)


    return "Não existe um Caminho"



