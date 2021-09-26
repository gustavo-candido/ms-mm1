import json
from validaEntrada import jsonValido

def main():
    with open("config.json", "r") as configArq:
        configJson = json.load(configArq)
    
    if not jsonValido(configJson):
        return False





if __name__ == "__main__":
    main()
