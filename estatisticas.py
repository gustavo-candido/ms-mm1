from tabulate import tabulate

class Estatisticas:
    def __init__(self):
        self.chegadas = []
        self.saidas = []
        self.ts = []

    def Adicionar_Chegada(self, t):
        self.chegadas.append(t)

    def Adicionar_saida(self, t):
        self.saidas.append(t)

    def Adicionar_ts(self, t):
        self.ts.append(t)

    def Imprime(self):
        cabecalho = ["ID", "TEC", "Hr_Chegada", "TS", "Inicio_Serviço", "Fim_Serviço", "Tempo_Fila", "Tempo_Sistema", "Tmp_Ocioso"]
        
        est = []
        tempo_ocioso = 0
        tf_acumulado = 0
        tempo_sistema_acumulado = 0
        for id in range(len(self.saidas)):
            tec = self.chegadas[id] if(id==0) else self.chegadas[id]-self.chegadas[id-1]
            tmp_ocioso = self.chegadas[id] if(id==0) else max(0, self.chegadas[id]-self.saidas[id-1])
            tempo_ocioso += tmp_ocioso
            tf = (self.saidas[id]-self.ts[id])-self.chegadas[id]
            tf = tf if(abs(tf)>1e-5) else 0
            a = [id+1, tec, self.chegadas[id], self.ts[id], self.saidas[id]-self.ts[id], self.saidas[id], tf, self.saidas[id]-self.chegadas[id], tmp_ocioso]
            est.append(a)
            tf_acumulado += tf
            tempo_sistema_acumulado += self.saidas[id]-self.chegadas[id]


        print(tabulate(est, cabecalho))
        print("Taxa Média de Ocupação do Servidor   =  {:.2f}".format((self.saidas[-1]-tempo_ocioso)/self.saidas[-1]))
        print("Tempo Médio de uma Entidade na Fila  =  {:.2f} min".format(tf_acumulado/len(self.saidas)))
        print("Tempo Medio no Sistema               =  {:.2f} min".format(tempo_sistema_acumulado/len(self.saidas)))
        