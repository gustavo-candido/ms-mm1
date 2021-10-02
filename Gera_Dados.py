from Distribuicoes import distribuicao

def geraTempo(
    distName: str,
    distArgs, 
) -> None:
    dados = []
    for i in range(100):
        ProximoTec = distribuicao(distName)(**distArgs)
        ProximoTec = (int) (ProximoTec*10)
        ProximoTec /= 10
        dados.append(ProximoTec)
    return dados