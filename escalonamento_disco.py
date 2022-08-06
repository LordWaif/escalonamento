import numpy as np
import sys
class Disco:
    def __init__(self):
        self.entrada = []
        '''with open('input.txt') as file:
            self.entrada = file.readlines()
            file.close()'''
        for l in sys.stdin:
            if l == '\n':
                break
            self.entrada.append(l)
        self.entrada = [int(i) for i in self.entrada]
        self.raio = self.entrada[0]
        self.pos_inicial = self.entrada[1]
        self.entrada = self.entrada[2:]

        self.error()
    def error(self):
        for i in self.entrada:
            if i > self.raio or i < 0:
                raise TypeError("Entrada invalida: ",i)
    def FCFS(self):
        distancia_total = 0
        pos_atual = self.pos_inicial
        for i in self.entrada:
            distancia_percorrida = abs(i-pos_atual)
            distancia_total += distancia_percorrida
            pos_atual = i
        return distancia_total

    def SSTF(self):
        distancia_total = 0
        entrada = np.array(self.entrada)
        pos_atual = self.pos_inicial
        while(len(entrada)!=0):
            diff = np.absolute(entrada-pos_atual)
            indice = diff.argmin()
            distancia_percorrida = abs(entrada[indice]-pos_atual)
            distancia_total += distancia_percorrida
            pos_atual = entrada[indice]
            entrada = np.delete(entrada,indice)
        return distancia_total

    def SCAN(self):
        distancias = np.absolute(np.array(sorted(self.entrada))-self.pos_inicial)
        return distancias[-1]*2+distancias[0]

escalonador = Disco()
print('FCFS',escalonador.FCFS())
print('SSTF',escalonador.SSTF())
print('ELEVADOR',escalonador.SCAN())