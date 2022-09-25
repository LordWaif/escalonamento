from audioop import add
from cgi import print_arguments
import numpy as np
import sys
from fila import Fila

class Pagina:
    def __init__(self,add,instante):
        self.addr = add
        self.bitRef = True
        self.instante = instante
        self.lastUse = instante
    def getAddr(self):
        return self.addr
    def getIntant(self):
        return self.instante
    def setbRef(self,bit):
        self.bitRef = bit
    def getbRef(self):
        return self.bitRef
    def getLastUse(self):
        return self.lastUse
    def setLastUse(self,instante):
        self.lastUse = instante
    def __str__(self) -> str:
        return str(self.addr)

class RAM:
    def __init__(self):
        self.entrada = []
        for l in sys.stdin:
            if l == '\n':
                break
            self.entrada.append(int(l))
        self.n_moldura = self.entrada[0]
        self.entrada = np.array(self.entrada[1:])
        self.copy_entrada = self.entrada.copy()

        self.error()
    def error(self):
        pass

    def SecondChance(self):
        falta_pags = self.n_moldura
        INSTANTE = 0
        paginas = []
        for i in self.entrada:
            if (INSTANTE+1)%4 == 0:
                for j in paginas:
                    j.setbRef(False)
            for j in paginas:
                if j.getAddr() == i:
                    j.setbRef(True)
            if len(paginas) < self.n_moldura:
                paginas.append(Pagina(i,INSTANTE))
            else:
               if len([j for j in paginas if i == j.getAddr()]) == 0:
                ind = 0
                while(True):
                    if ind == len(paginas):
                        ind == 0
                    if paginas[ind].getbRef() == True:
                        paginas[ind].setbRef(False)
                    else:
                        falta_pags += 1
                        paginas[ind] = Pagina(i,INSTANTE)
                        break
                    ind+=1
            INSTANTE +=1
        return falta_pags

    def Otimo(self):
        falta_pags = self.n_moldura
        INSTANTE = 0
        paginas = []
        for i,elem in enumerate(self.entrada):
            if len(paginas) < self.n_moldura:
                paginas.append(Pagina(elem,INSTANTE))
            else:
                if len([j for j in paginas if elem == j.getAddr()]) == 0:
                    switch = -1
                    maior = 0
                    for k in range(len(paginas)):
                        not_ref = set([i.getAddr() for i in paginas]).difference(set(self.entrada[i+1:]))
                        if len(not_ref) != 0:
                            switch = [i.getAddr() for i in paginas].index(list(not_ref)[0])
                            break
                        for j in range(len(self.entrada[i+1:])):
                            if(self.entrada[i+1:][j]==paginas[k].getAddr()):
                                if j>maior:
                                    switch = k
                    falta_pags += 1
                    paginas[switch] = Pagina(elem,INSTANTE)
            INSTANTE +=1
        return falta_pags

    def ConjTrabalho(self):
        falta_pags = self.n_moldura
        limiar = (self.n_moldura//2)+1
        INSTANTE = 0
        paginas = []
        for i in self.entrada:
            #print('Referencia: ',i,' Ints: ',INSTANTE)
            if len(paginas) < self.n_moldura:
                paginas.append(Pagina(i,INSTANTE))
            else:
                maior_idade,ind_maior = -1,-1
                isSwitch = False
                falta = (len([j for j in paginas if i == j.getAddr()]) == 0)
                for ind in range(len(paginas)):
                    if falta:
                        if paginas[ind].getbRef() == True:
                            paginas[ind].setLastUse(INSTANTE)
                        else:
                            if (INSTANTE - paginas[ind].getLastUse()) > limiar:
                                #print('Saiu: ',paginas[ind].getAddr(),' Entrou: ',i)
                                falta_pags += 1
                                isSwitch = True
                                paginas[ind] = Pagina(i,INSTANTE)
                            else:
                                if(INSTANTE - paginas[ind].getLastUse()) > maior_idade:
                                    ind_maior = ind
                                    maior_idade = INSTANTE - paginas[ind].getLastUse()
                    else:
                        if(paginas[ind].getAddr()==i):
                            paginas[ind].setLastUse(INSTANTE)
                            paginas[ind].setbRef(True)
                if falta and not(isSwitch):
                    falta_pags += 1
                    paginas[ind_maior] = Pagina(i,INSTANTE)
            #print([[i.getAddr(),i.getbRef(),i.getLastUse(),INSTANTE-i.getLastUse()] for i in paginas])
            INSTANTE +=1
            if (INSTANTE)%4 == 0:
                #print('Zerando bitRef')
                for j in paginas:
                    j.setbRef(False)
                #print([[i.getAddr(),i.getbRef(),i.getLastUse(),INSTANTE-i.getLastUse()] for i in paginas])
                #print('--------------')
        return falta_pags

escalonador = RAM()
sc = escalonador.SecondChance()
o = escalonador.Otimo()
ct = escalonador.ConjTrabalho()
print('SC {:.0f}'.format(sc))
print('OTM {:.0f}'.format(o))
print('CT {:.0f}'.format(ct))