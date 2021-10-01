import json
from Simulacao import simulador
import MonteCarloTec
import MonteCarloTs
from Estatisticas import Imprime
from Gera_Dados import gera_tec, gera_ts

def main():
    with open("config/parametros-simulacao.json", "r") as arqConfig:
        paramSimulacao = json.load(arqConfig)
    
    # ** unpack operator https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

    dados_tec = gera_tec(**paramSimulacao)
    dados_ts = gera_ts(**paramSimulacao)
    MonteCarloTec.Definicao(dados_tec)
    MonteCarloTs.Definicao(dados_ts)
    simulador(**paramSimulacao)
    Imprime()
    
    
if __name__ == "__main__":
    main()
