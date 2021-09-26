suportDist=["deterministico"]

def validDist(distTip, params):
    if distTip == "deterministico" and not isinstance(params, int):
        print("Erro de tipo! A distribuição deterministica precisa ser um inteiro\n")
        return False

    return True

def validValores(json): 
    if not isinstance(json["nClientes"], int): 
        print("Erro de tipo!\nnClientes precisa ser inteiro\n")
        return False
    
    if not isinstance(json["tec"], int): 
        print("Erro de tipo!\ntec precisa ser inteiro\n")
        return False

    if not isinstance(json["ts"], int): 
        print("Erro de tipo!\nts precisa ser inteiro\n")
        return False

    if not isinstance(json["filaMax"], int): 
        print("Erro de tipo!\nfilaMax precisa ser inteiro\n")
        return False

    if not isinstance(json["tecDist"], str) or  json["tecDist"] not in suportDist: 
        print("Erro de tipo!\ntecDist precisa ser \"deterministico\"\n")
        return False

    if not isinstance(json["tsDist"], str) or  json["tsDist"] not in suportDist: 
        print("Erro de tipo!\ntsDist precisa ser \"deterministico\"\n")
        return False

    return validDist(json["tecDist"], json["ts"]) and validDist(json["tsDist"], json["ts"])

def validParam(json):
    if "nClientes" not in json: 
        print("nClientes<int> precisa ser informado\n")
        return False

    if "filaMax" not in json: 
        print("filaMax<int> precisa ser informado\n")
        return False

    if "tecDist" not in json: 
        print("tecDist<String> precisa ser informado\n")
        return False

    if "tec" not in json: 
        print("tec<int> precisa ser informado\n")
        return False

    if "tsDist" not in json: 
        print("tsDist<string> precisa ser informado\n")
        return False

    if "ts" not in json: 
        print("ts<int> precisa ser informado\n")
        return False
    
    return True

def jsonValido(json): 
    if not validParam(json):
        return False

    if not validValores(json):
        return False

    return True