import math
import bisect
from NumeroAleatorio import nAleatorio

class classe:
    mini: float
    maxi: float
    quant: int
    media: float
    max_decimal: float

class MonteCarlo: 
    def __init__(self, dados):
        dados.sort()
        self.dados = dados
        self.vetor_classes = []
        self.max_d = []

    def geraClasses(self):
        tam = len(self.dados)
        minimo = self.dados[0]
        maximo = self.dados[-1]

        k = round(1+3.3*math.log10(tam))
        tamanho_classe = (maximo-minimo)/k

        lim = minimo+tamanho_classe
        while(True):
            a = classe()
            a.maxi = lim
            a.mini = lim-tamanho_classe
            a.quant = 0
            a.media = (a.mini+a.maxi)/2
            a.media = (int) (a.media*100)
            a.media = a.media/100

            self.vetor_classes.append(a)
            if(lim>=maximo): break
            lim += tamanho_classe

        idx = 0
        for dado in self.dados:
            while(dado>=self.vetor_classes[idx].maxi and dado!=self.vetor_classes[-1].maxi):
                idx += 1

            self.vetor_classes[idx].quant += 1
        
        for i in range(len(self.vetor_classes)):
            if(i>0): self.vetor_classes[i].max_decimal = self.vetor_classes[i-1].max_decimal
            else: self.vetor_classes[i].max_decimal = 0.0

            self.vetor_classes[i].max_decimal += self.vetor_classes[i].quant/len(self.dados)
            self.max_d.append(self.vetor_classes[i].max_decimal)

        return

    def geraNumero(self):
        num = nAleatorio()
        if len(self.vetor_classes)==0:
            print("É preciso definir os dados do Monte Carlo antes!")
            return
        idx = bisect.bisect_left(self.max_d, num)
        return self.vetor_classes[idx].media
