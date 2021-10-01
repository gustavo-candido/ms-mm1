import math
import bisect

class classe:
    mini: float
    maxi: float
    quant: int
    media: float
    max_decimal: float

vetor_classes = []
max_d = []

def Definicao(dados):

    vetor_classes.clear()
    dados.sort()
    tam = len(dados)
    minimo = dados[0]
    maximo = dados[-1]

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

        vetor_classes.append(a)
        if(lim>=maximo): break
        lim += tamanho_classe
    

    idx = 0
    for dado in dados:
        while(dado>=vetor_classes[idx].maxi and dado!=vetor_classes[-1].maxi):
            idx += 1

        vetor_classes[idx].quant += 1
    
    for i in range(len(vetor_classes)):
        if(i>0): vetor_classes[i].max_decimal = vetor_classes[i-1].max_decimal
        else: vetor_classes[i].max_decimal = 0.0

        vetor_classes[i].max_decimal += vetor_classes[i].quant/len(dados)
        max_d.append(vetor_classes[i].max_decimal)

    return

def Aplicacao(num):
    if len(vetor_classes)==0:
        print("É preciso definir os dados do Monte Carlo antes!")
        return
    # print("num = {}".format(num))
    idx = bisect.bisect_left(max_d, num)
    return vetor_classes[idx].media