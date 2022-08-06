import numpy as np
import sys
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
        pass

        self.error()
    def error(self):
        pass
    def PRI(self):
        EXECUTADOS = []
        RETORNO_MEDIO,RESPOSTA_MEDIA,ESPERA_MEDIA = [],[],[]
        INSTANTE = 0
        while(np.sum(self.entrada[:,1]) !=0):
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
        return sum(RETORNO_MEDIO)/len(RETORNO_MEDIO),sum(RESPOSTA_MEDIA)/len(RESPOSTA_MEDIA),sum(ESPERA_MEDIA)/len(ESPERA_MEDIA)
       
escalonador = CPU()
pri = escalonador.PRI()
print('PRI {:.2f} {:.2f} {:.2f}'.format(pri[0],pri[1],pri[2]))