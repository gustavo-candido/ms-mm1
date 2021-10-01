from tabulate import tabulate

chegadas = []
saidas = []
ts = []

def Adicionar_Chegada(t):
    chegadas.append(t)

def Adicionar_saida(t):
    saidas.append(t)

def Adicionar_ts(t):
    ts.append(t)

def Imprime():
    # print("saidas = ", end="")
    # print(saidas)
    # cabecalho = ["chegada", "ts", "saida"]
    # k = []
    # for i in range(len(saidas)):
    #     a = [chegadas[i], ts[i], saidas[i]]
    #     k.append(a)
    # print(tabulate(k, cabecalho))

    # print("\n\n")
    cabecalho = ["ID", "TEC", "Hr_Chegada", "TS", "Inicio_Serviço", "Fim_Serviço", "Tempo_Fila", "Tempo_Sistema", "Tmp_Ocioso"]
    
    est = []
    for id in range(len(saidas)):
        tec = chegadas[id] if(id==0) else chegadas[id]-chegadas[id-1]
        tmp_ocioso = chegadas[id] if(id==0) else max(0, chegadas[id]-saidas[id-1])

        a = [id+1, tec, chegadas[id], ts[id], saidas[id]-ts[id], saidas[id], (saidas[id]-ts[id])-chegadas[id], saidas[id]-chegadas[id], tmp_ocioso]
        est.append(a)

    print(tabulate(est, cabecalho))