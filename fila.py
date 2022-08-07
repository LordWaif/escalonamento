import numpy as np

class Fila:
    def __init__(self,entrada):
        self.lista = entrada

    def getHead(self):
        return self.lista[0]

    def setHead(self,head):
        self.lista[0] = head

    def consume(self):
        head = self.getHead()
        self.lista = np.append(np.delete(self.lista,0,axis=0),[head],axis=0)

    def removeZeros(self):
        self.lista = np.delete(self.lista,np.where(self.lista[:,1]==0),axis=0)

    def getAll(self):
        return self.lista

