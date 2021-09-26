import json
from Simulacao import simulador

def main():
    with open("config/parametros-simulacao.json", "r") as arqConfig:
        paramSimulacao = json.load(arqConfig)
    
    # ** unpack operator https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
    simulador(**paramSimulacao)
    
if __name__ == "__main__":
    main()

# testeeeeee