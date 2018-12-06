'''Import Interface Gráfica'''
from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

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

        self.tiposBusca = ['Busca em largura', 'Busca em largura melhor caminho', 'Busca em Profundidade', 'A*']

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
            self.caminho['text'] = busca_largura(self.grafo, self.de.get(), self.para.get())

        elif self.tipo.get() == 'Busca em largura melhor caminho':
            self.caminho['text'] = busca_largura_melhorCaminho(self.grafo, self.de.get(), self.para.get())

        elif self.tipo.get() == 'Busca em Profundidade':
            self.caminho['text'] = busca_profundidade(self.grafo, self.de.get(), self.para.get())

        elif self.tipo.get() == 'A*':
            self.caminho['text'] = aAsterisco(self.grafo, self.ordemCidades, self.matrizDist, self.de.get(), self.para.get())

        else:
            self.caminho['text'] = 'Opção Inválida'



def main():
    ordemCidades, matrizDist = getDistanciaTotal()
    grafo = getGrafo()

    root = Tk() #Cria a janela
    root.title('Agentes de Busca') #Seta título da janela
    root.geometry('600x300') #Seta tamanho inicial da janela

    Application(ordemCidades, matrizDist, grafo, root)
    root.mainloop()


main()