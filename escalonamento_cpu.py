#%%
import numpy as np
import sys
import random as rd
from fila import Fila
from io import StringIO

class CPU:
    def __init__(self):
        self.entrada = []
        count = 0
        for l in sys.stdin:
            chegada,duração = l.split(' ')
            if l == '\n':
                break
            self.entrada.append([int(chegada),int(duração),1,count,int(duração)])
            count+=1
        self.entrada = np.array(self.entrada)
        self.copy_entrada = self.entrada.copy()

        self.error()
    def error(self):
        pass
    def PRI(self):
        EXECUTADOS = []
        RETORNO_MEDIO,RESPOSTA_MEDIA,ESPERA_MEDIA = [],[],[]
        INSTANTE = 0
        self.entrada = self.entrada[self.entrada[:, 0].argsort()]
        while(np.sum(self.entrada[:,1]) !=0):
            prontos = self.entrada[np.where(self.entrada[:,0] <= INSTANTE)]
            while(len(prontos)==0):
                INSTANTE += 1
                prontos = self.entrada[np.where(self.entrada[:,0] <= INSTANTE)]
            indice_maior = np.argmax(prontos[:,2])
            if self.entrada[indice_maior,3] not in EXECUTADOS:
                RESPOSTA_MEDIA.append(INSTANTE-self.entrada[indice_maior,0])
                EXECUTADOS.append(self.entrada[indice_maior,3])
            # Executando
            self.entrada[:,2] += 1
            self.entrada[indice_maior,2] -= 2
            self.entrada[indice_maior,1] -= 1
            INSTANTE += 1
            if self.entrada[indice_maior,1] == 0:
                RETORNO_MEDIO.append(INSTANTE - self.entrada[indice_maior,0])
                ESPERA_MEDIA.append(INSTANTE - self.entrada[indice_maior,0] - self.entrada[indice_maior,4])
                self.entrada = np.delete(self.entrada,indice_maior,axis=0)
        self.entrada = self.copy_entrada.copy()
        return np.mean(RETORNO_MEDIO),np.mean(RESPOSTA_MEDIA),np.mean(ESPERA_MEDIA)
    
    def LOTERIA(self):
        EXECUTADOS = []
        EXCLUIDOS = []
        RETORNO_MEDIO,RESPOSTA_MEDIA,ESPERA_MEDIA = [],[],[]
        INSTANTE = 0
        while(np.sum(self.entrada[:,1]) !=0):
            if not(any(self.entrada[:,0]<=INSTANTE)):
                INSTANTE += 1
                continue
            valores_possiveis = self.entrada[np.where(self.entrada[:,0] <=INSTANTE),3]
            escolhido = rd.choice(valores_possiveis[0])            
            indice = np.where(self.entrada[:,3] == escolhido)
            if self.entrada[indice,3] not in EXECUTADOS:
                RESPOSTA_MEDIA.append(INSTANTE-self.entrada[indice,0])
                EXECUTADOS.append(self.entrada[indice,3])
            # Executando
            self.entrada[indice,1] -= 1
            INSTANTE += 1
            if self.entrada[indice,1] == 0:
                RETORNO_MEDIO.append(INSTANTE - self.entrada[indice,0])
                ESPERA_MEDIA.append(INSTANTE - self.entrada[indice,0] - self.entrada[indice,4])
                EXCLUIDOS.append(self.entrada[indice,3])
                self.entrada = np.delete(self.entrada,indice,axis=0)
        self.entrada = self.copy_entrada.copy()
        return np.mean(RETORNO_MEDIO),np.mean(RESPOSTA_MEDIA),np.mean(ESPERA_MEDIA)

    def RoundRobin(self,quantum):
        from graphs import GraphGenerate
        EXECUTADOS = []
        EXCLUIDOS = []
        RETORNO_MEDIO,RESPOSTA_MEDIA,ESPERA_MEDIA = [],[],[]
        #self.entrada = self.entrada[self.entrada[:, 0].argsort()]
        fila_circular = Fila(self.entrada)
        qtd = len(self.entrada)
        QUANTUM = quantum
        INSTANTE = 0
        HISTORY = []
        while(np.sum(fila_circular.getAll()[:,1]) !=0):
            processo = fila_circular.getHead()
            if processo[0] > INSTANTE:
                fila_circular.consume()
                processo_c = fila_circular.getHead()
                is_ready = False
                while(processo[3]!=processo_c[3]):
                    if processo_c[0]<INSTANTE:
                        is_ready = True
                        break
                    else:
                        fila_circular.consume()
                        processo_c = fila_circular.getHead()
                if not(is_ready):
                    INSTANTE += 1
                    continue
                else:
                    processo = processo_c
            int_ini = processo[1]
            if processo[1] >= QUANTUM:
                processo[1] -= QUANTUM
            else:
                processo[1] = 0
            int_fin = processo[1]
            fila_circular.setHead(processo)
            fila_circular.consume()
            if processo[3] not in EXECUTADOS:
                RESPOSTA_MEDIA.append(INSTANTE-processo[0])
                EXECUTADOS.append(processo[3])
            INSTANTE += abs(int_fin - int_ini)
            if processo[1] == 0:
                RETORNO_MEDIO.append(INSTANTE - processo[0])
                ESPERA_MEDIA.append(INSTANTE - processo[0] - processo[4])
                EXCLUIDOS.append(processo[3])
                fila_circular.removeZeros()
            HISTORY.append(list(processo)+[INSTANTE,abs(int_fin - int_ini)])
        try:
            GraphGenerate().graphCPU('RR',INSTANTE,HISTORY,qtd)
        except:
            pass
        self.entrada = self.copy_entrada.copy()
        return np.mean(RETORNO_MEDIO),np.mean(RESPOSTA_MEDIA),np.mean(ESPERA_MEDIA)

escalonador = CPU()
pri = escalonador.PRI()
lot = escalonador.LOTERIA()
rr = escalonador.RoundRobin(2)
print('PRI {:.2f} {:.2f} {:.2f}'.format(pri[0],pri[1],pri[2]))
print('LOT {:.2f} {:.2f} {:.2f}'.format(lot[0],lot[1],lot[2]))
print('RR {:.2f} {:.2f} {:.2f}'.format(rr[0],rr[1],rr[2]))
# %%