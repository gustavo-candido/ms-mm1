from estatisticas import Estatisticas
from monteCarlo import MonteCarlo
from math import inf
from Distribuicoes import distribuicao
from NumeroAleatorio import nAleatorio
from Gera_Dados import geraTempo

def simulador(
    nClientes: int,
    filaMax: int,
    tecDist: str,
    tecArgs, 
    tsDist: str,
    tsArgs 
) -> None:
    if tecDist!='deterministica':
        dados_tec = geraTempo(tecDist, tecArgs)
        monteCarloTec = MonteCarlo(dados_tec)
        monteCarloTec.geraClasses()
    
    if tsDist!='deterministica':
        dados_ts = geraTempo(tsDist, tsArgs)
        monteCarloTs = MonteCarlo(dados_ts)
        monteCarloTs.geraClasses()

    return executaSimulacao(
        nClientes=nClientes,
        filaMax=filaMax,
        proximoTec=lambda: distribuicao('deterministica')(**tecArgs) if(tecDist=='deterministica') else monteCarloTec.geraNumero(),
        proximoTs=lambda: distribuicao('deterministica')(**tsArgs) if(tsDist=='deterministica') else monteCarloTs.geraNumero(),
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
    ultimo_evento_fila = 0
    media_pessoas_fila = 0

    hc = tr + proximoTec()
    estatisticas = Estatisticas()
    estatisticas.Adicionar_Chegada(hc)

    cliente = 1
    while(cliente<=nClientes):
        if(hc<=hs):      # próxima chegada acontece antes de próxima saída
            tr = hc
            if(tf<filaMax):
                if not ocupado:
                    ocupado = True
                    ts = proximoTs()
                    estatisticas.Adicionar_ts(ts)
                    hs = tr + ts
                    
                else:
                    media_pessoas_fila += (tr-ultimo_evento_fila)*tf
                    ultimo_evento_fila = tr
                    tf += 1
            hc = tr + proximoTec()
            estatisticas.Adicionar_Chegada(hc)

        else:
            tr = hs
            estatisticas.Adicionar_saida(hs)
            cliente += 1

            if(tf>0):
                tf -= 1
                media_pessoas_fila += (tr-ultimo_evento_fila)*tf
                ultimo_evento_fila = tr
                ts = proximoTs()
                estatisticas.Adicionar_ts(ts)
                hs = tr + ts
            else:
                ocupado = False
                hs = 99999999999

    estatisticas.Imprime()
    media_pessoas_fila /= tr
    print("Número Médio de Entidades na Fila    =  {:.2f}".format(media_pessoas_fila))
