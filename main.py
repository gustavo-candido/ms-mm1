import json
from Simulacao import simulador
from MonteCarlo import Aplicacao, Definicao
import Estatisticas

def main():
    with open("config/parametros-simulacao.json", "r") as arqConfig:
        paramSimulacao = json.load(arqConfig)
    
    # ** unpack operator https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
    dados = [1,2,3,4,5,6,7,8,9,10]
    Definicao(dados)
    simulador(**paramSimulacao)
    Estatisticas.Imprime()
    
    
if __name__ == "__main__":
    main()
