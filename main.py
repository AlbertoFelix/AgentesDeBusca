'''Import Interface Gráfica'''
from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''Import Algorítmos de Busca'''
from Grafo import *
from buscaProfundidade import *
from BuscaEmLargura import *
from BuscaAAsterisco import *

class Application:
    def __init__(self, ordemCidades, matrizDist, grafo, master=None):
        self.ordemCidades = ordemCidades
        self.matrizDist = matrizDist
        self.grafo = grafo
        self.tracarCaminho = False
        self.rota = None
        self.drawGrafo = self.showGrafo(self.tracarCaminho, self.rota)

        self.tiposBusca = ['Busca em largura', 'Busca em Profundidade', 'A*']

        '''Frame com De e Para'''
        self.frame1 = Frame(master)
        self.frame1.pack(side=TOP, fill=X)

        #Label De
        self.deLabel = Label(self.frame1, text='De:')
        self.deLabel.pack(side=LEFT, anchor=W)

        #ComboBox selecionar De
        self.de = StringVar()
        self.comboDe = Combobox(self.frame1, values=self.ordemCidades, textvariable=self.de)
        self.comboDe.set('Selecione...')
        self.comboDe['state'] = 'readonly'
        self.comboDe.pack(side=LEFT, anchor=W, fill=X, expand=True)

        #Label Para
        self.paraLabel = Label(self.frame1, text='Para:')
        self.paraLabel.pack(side=LEFT, anchor=W)

        #ComboBox selecionar Para
        self.para = StringVar()
        self.comboPara = Combobox(self.frame1, values=self.ordemCidades, textvariable=self.para)
        self.comboPara.set('Selecione...')
        self.comboPara['state'] = 'readonly'
        self.comboPara.pack(side=LEFT, anchor=W, fill=X, expand=True)

        '''Frame com o caminho'''
        self.frame2 = Frame(master)
        self.frame2["pady"] = 10
        self.frame2.pack()

        #Label Caminho
        self.caminho = Label(self.frame2, text='')
        self.caminho.pack()

        #Grafo
        self.canvas = FigureCanvasTkAgg(self.drawGrafo, master=self.frame2)
        self.canvas.get_tk_widget().pack(side=TOP, anchor=W, fill=BOTH, expand=True)

        '''Frame com o tipo de busca e o botão de Buscar'''
        self.frame3 = Frame(master)
        self.frame3["pady"] = 10
        self.frame3.pack(side=BOTTOM, fill=X)

        #Label Tipo de Busca
        self.labelTipo = Label(self.frame3, text='Tipo de Busca:')
        self.labelTipo.pack(side=LEFT, anchor=W)

        #ComboBox selecionar Tipo de Busca
        self.tipo = StringVar()
        self.comboTipoBusca = Combobox(self.frame3, values=self.tiposBusca, textvariable=self.tipo)
        self.comboTipoBusca.set('Selecione...')
        self.comboTipoBusca['state'] = 'readonly'
        self.comboTipoBusca.pack(side=LEFT, anchor=W, expand=True, fill=X)

        #Botão Buscar
        self.buscar = Button(self.frame3, text='Buscar', command=self.buscarCaminho, width=10)
        self.buscar.pack(side=RIGHT, anchor=E)

    def buscarCaminho(self):
        if self.tipo.get() == 'Busca em largura':
            self.tracarCaminho = True
            self.rota = busca_largura_melhorCaminho(self.grafo, self.de.get(), self.para.get()) #Define a nova Rota

            self.caminho['text'] = self.getCaminho(self.rota)
            self.drawGrafo = self.showGrafo(self.tracarCaminho, self.rota) #Define o novo grafo
            self.canvas.draw() #Desenha o novo grafo

        elif self.tipo.get() == 'Busca em Profundidade':
            self.tracarCaminho = True
            self.rota = busca_profundidade(self.grafo, self.de.get(), self.para.get()) #Define a nova Rota

            self.caminho['text'] = self.getCaminho(self.rota)
            self.drawGrafo = self.showGrafo(self.tracarCaminho, self.rota) #Define o novo grafo
            self.canvas.draw() #Desenha o novo grafo

        elif self.tipo.get() == 'A*':
            self.tracarCaminho = True
            self.rota = aAsterisco(self.grafo, self.ordemCidades, self.matrizDist, self.de.get(), self.para.get()) #Define a nova Rota

            self.caminho['text'] = self.getCaminho(self.rota)
            self.drawGrafo = self.showGrafo(self.tracarCaminho, self.rota) #Define o novo grafo
            self.canvas.draw() #Desenha o novo grafo

        else:
            self.caminho['text'] = 'Opção Inválida'

    def getCaminho(self, caminho):
        rota = ''
        for i in range(len(caminho)):
            if i == len(caminho) - 1:
                rota += caminho[i]
            else:
                rota += caminho[i]
                rota += '=> '

        return rota

    def showGrafo(self, tracarCaminho, rota):
        plt.cla()
        f = plt.figure(8, figsize=(17, 7))  # definindo o tamanho da figura
        pos = nx.fruchterman_reingold_layout(self.grafo)  # definindo o algoritmo do layout
        plt.axis('off')  # retira as bordas
        nx.draw_networkx_nodes(self.grafo, pos, node_size=180, node_color='cyan') #Plota os nos
        nx.draw_networkx_edges(self.grafo, pos, alpha=0.8)  #Plota as arestas
        nx.draw_networkx_labels(self.grafo, pos, font_size=9) #Coloca o nome nas cidades

        if tracarCaminho == True:
            self.mostrarCaminho(self.grafo, pos, rota)

        return f

    def mostrarCaminho(self, grafo, pos, rota):
        edges = [(rota[n], rota[n + 1]) for n in range(len(rota) - 1)]
        nx.draw_networkx_edges(grafo, pos=pos, edgelist=edges, edge_color='yellow', width=4.0, alpha=0.5) #Pinta o caminho de amarelo
        nx.draw_networkx_nodes(grafo, pos, nodelist=[rota[0]], node_size=80, node_color='green') #Pinta o ponto inicial como Verde
        nx.draw_networkx_nodes(grafo, pos, nodelist=[rota[-1]], node_size=80, node_color='red') #Pinta o ponto final de Vermelho

def main():
    ordemCidades, matrizDist = getDistanciaTotal()
    grafo = getGrafo()

    root = Tk() #Cria a janela
    root.title('Agentes de Busca') #Seta título da janela
    root.geometry('1350x850') #Seta tamanho inicial da janela

    Application(ordemCidades, matrizDist, grafo, root)
    root.mainloop()


main()