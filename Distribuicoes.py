from NumeroAleatorio import nAleatorio
from math import pi, log, sqrt, cos, sin
import Valida

def deterministica(valor:float) -> float:
    return valor 

def uniforme(
    min: float,
    max: float,
) -> float:
    al=nAleatorio()
    return min+al*(max-min)

valores = [-1, -1]

def normal(
    media: float,
    desvio: float,
) -> float:
    
    if valores[0] == -1:
        r1 = nAleatorio()
        r2 = nAleatorio()
        valores[0] = cos(2 * pi * r2)*sqrt(-2 * log(r1))
        valores[1] = sin(2 * pi * r2)*sqrt(-2 * log(r1))

        return desvio*valores[0] + media
    
    else:
        valores[0] = -1
        return desvio*valores[1] + media


def exponencial(lamb: float) -> float:
    r = nAleatorio()
    return -(log(1 - r)/lamb)

# retorno é uma função de distribuição
def distribuicao(nomeDist:str): 
    mapaNomeParaFunc = {
        "deterministica": deterministica,
        "exponencial": exponencial,
        "normal": normal,
        "uniforme": uniforme,
    }
    Valida.tipoDistribuicao(mapaNomeParaFunc, nomeDist)
    return mapaNomeParaFunc[nomeDist]