#%%
from matplotlib import pyplot as plt

class GraphGenerate():
    def __ini__():
        pass
    def graphCPU(self,titulo,total_tempo_executado,historia,qtd_processos):
        fig, gnt = plt.subplots() 
        gnt.set_ylim(0, qtd_processos*10) 
        gnt.set_xlim(0, total_tempo_executado*10) 
        gnt.set_xlabel('tempo') 
        gnt.set_ylabel('Processos') 
        gnt.grid(True)
        inicio_final = []
        posicao = []
        for i in historia:
            duracao = i[6]
            inicio_final.append(tuple([(i[5]-duracao)*10,duracao*10]))
            posicao.append(tuple([i[3]*2.5,2]))
        cor = ['tab:blue']
        for processos in range(len(historia)):
            gnt.broken_barh([inicio_final[processos]], posicao[processos], facecolors = cor[0])
        fig.show()
        fig.savefig(titulo+'.png',format='png')
# %%
