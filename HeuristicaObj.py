class heuristicaObj():
    def __init__(self, ordemCidades, matrizDist):
        self.ordemCidades = ordemCidades
        self.matrizDist = matrizDist

    def getDistancia(self, cidade1, cidade2):
        c1 = None
        c2 = None
        for i in range(len(self.ordemCidades)):
            if cidade1 == self.ordemCidades[i]:
                c1 = i
            if cidade2 == self.ordemCidades[i]:
                c2 = i

        return self.matrizDist[c2][c1]
