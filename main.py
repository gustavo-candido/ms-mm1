import json
from Simulacao import simulador
from Estatisticas import Imprime


from Simulacao import executaSimulacao

tec = [15, 12, 10, 10, 12, 15, 10, 12, 10, 10, 10, 12, 15, 12, 12]
ts = [11,10,9,10,9,10,11,9,11,10,11,9,10,9,11]

def nextTec():
    if len(tec) == 0:
        return 99999999999
    ans = tec[0]
    tec.pop(0)
    return ans

def nextTs():
    if len(ts) == 0:
        return 0
    ans = ts[0]
    ts.pop(0)
    return ans

def faker():
    executaSimulacao(
    nClientes=15,
    filaMax=15,
    proximoTec=nextTec, # ()->float
    proximoTs=nextTs
    )



def main():
    with open("config/parametros-simulacao.json", "r") as arqConfig:
        paramSimulacao = json.load(arqConfig)
    
        if "filaMax" in paramSimulacao and  paramSimulacao["filaMax"] == "inf":
            paramSimulacao["filaMax"] = paramSimulacao["nClientes"]

    simulador(**paramSimulacao)
    
    
if __name__ == "__main__":
    main()
    # faker()