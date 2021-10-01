from Distribuicoes import distribuicao

def gera_tec(
    nClientes: int,
    filaMax: int,
    tecDist: str,
    tecArgs, 
    tsDist: str,
    tsArgs 
) -> None:
    dados_tec = []
    for i in range(100):
        ProximoTec = distribuicao(tecDist)(**tecArgs)
        ProximoTec = (int) (ProximoTec*10)
        ProximoTec /= 10
        dados_tec.append(ProximoTec)
    return dados_tec

def gera_ts(
    nClientes: int,
    filaMax: int,
    tecDist: str,
    tecArgs, 
    tsDist: str,
    tsArgs 
) -> None:
    dados_ts = []
    for i in range(100):
        ProximoTs = distribuicao(tsDist)(**tsArgs)
        ProximoTs = (int) (ProximoTs*10)
        ProximoTs = ProximoTs/10
        dados_ts.append(ProximoTs)
    return dados_ts