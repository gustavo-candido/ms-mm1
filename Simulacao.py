from Distribuicoes import distribuicao

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
    print('simulando...')
    print("nClientes: " + str(nClientes) )
    print("filaMax: " + str(filaMax) )
    print("proximoTec: " + str(proximoTec()))
    print("proximoTec: " + str(proximoTec()))
    print("proximoTs: " + str(proximoTs()))
    print('fim')