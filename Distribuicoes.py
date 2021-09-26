from NumeroAleatorio import nAleatorio
import Valida

def deterministica(valor:float) -> float:
    return valor 

def uniforme(
    min: float,
    max: float,
) -> float:
    al=nAleatorio()
    return min+al*(max-min)

# retorno é uma função de distribuição
def distribuicao(nomeDist:str): 
    mapaNomeParaFunc = {
        "deterministica": deterministica,
        "uniforme": uniforme,
    }
    Valida.tipoDistribuicao(mapaNomeParaFunc, nomeDist)
    return mapaNomeParaFunc[nomeDist]