import json
from validaEntrada import jsonValido
import geradores

def instanciaGerador(gerTipo, param):
    if gerTipo == "deterministico":
        return geradores.GeradorDeterministico(param)
    
    raise Exception("Gerador inválido")


def main():
    with open("config.json", "r") as configArq:
        configJson = json.load(configArq)
    
    if not jsonValido(configJson):
        return False

    geradorTec = instanciaGerador(configJson["tecDist"], configJson["tec"])
    geradorTs = instanciaGerador(configJson["tsDist"], configJson["ts"])



if __name__ == "__main__":
    main()
