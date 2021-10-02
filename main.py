import json
from Simulacao import simulador

from Simulacao import executaSimulacao


def main():
    with open("config/parametros-simulacao.json", "r") as arqConfig:
        paramSimulacao = json.load(arqConfig)
    
        if "filaMax" in paramSimulacao and  paramSimulacao["filaMax"] == "inf":
            paramSimulacao["filaMax"] = paramSimulacao["nClientes"]

    simulador(**paramSimulacao)
    
    
if __name__ == "__main__":
    main()