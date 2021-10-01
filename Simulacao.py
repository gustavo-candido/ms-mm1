from math import inf
from Distribuicoes import distribuicao
from MonteCarlo import Aplicacao
from NumeroAleatorio import nAleatorio
import Estatisticas

def simulador(
    nClientes: int,
    filaMax: int,
    tecDist: str,
    tecArgs, 
    tsDist: str,
    tsArgs 
) -> None:
    return executaSimulacao(
        nClientes=nClientes,
        filaMax=filaMax,
        proximoTec=lambda: distribuicao(tecDist)(**tecArgs),
        proximoTs=lambda: distribuicao(tsDist)(**tsArgs),
    )

def executaSimulacao(
    nClientes: int,
    filaMax: int,
    proximoTec, # ()->float
    proximoTs, # ()->float
) -> None:

    tr = 0 # tempo atual
    ocupado = False # estado do servidor
    tf = 0 # tamanho da fila
    hc = 0 # hora do próximo evento de chegada
    hs = 99999999999 # hora do próximo evento de saída
    tf = 0 # tamanho da fila

    # aqui = proximoTec()
    # print("aqui = {}".format(aqui))
    # aqui2 = Aplicacao(aqui)
    # print("aqui2 = {}".format(aqui2))
    
    hc = tr + Aplicacao(nAleatorio())
    Estatisticas.Adicionar_Chegada(hc)

    cliente = 1
    while(cliente<=15):
        if(hc<hs):      # próxima chegada acontece antes de próxima saída
            tr = hc
            if not ocupado:
                ocupado = True
                ts = Aplicacao(nAleatorio())
                Estatisticas.Adicionar_ts(ts)
                hs = tr + ts
                
            else:
                tf += 1
            hc = tr + Aplicacao(nAleatorio())
            Estatisticas.Adicionar_Chegada(hc)

        else:
            tr = hs
            Estatisticas.Adicionar_saida(hs)
            cliente += 1

            if(tf>0):
                tf -= 1
                ts = Aplicacao(nAleatorio())
                Estatisticas.Adicionar_ts(ts)
                hs = tr + ts
            else:
                ocupado = False
                hs = 99999999999

        
        # break



    # print('simulando...')
    # print("nClientes: " + str(nClientes) )
    # print("filaMax: " + str(filaMax) )
    # print("proximoTec: " + str(proximoTec()))
    # print("proximoTec: " + str(proximoTec()))
    # print("proximoTs: " + str(proximoTs()))
    # print('fim')