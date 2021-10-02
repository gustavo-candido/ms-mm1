# Documentação

Além das informações neste arquivo, recomenda-se a leitura do arquivo `readme.md`.

## parametros-simulacao.json

Contém a configuração da simulação no formato json. As insformações a respeito dos parâmetros suportados estão descritas no arquivo `README.md`.

## main.py

Arquivo de execução do programa. Responsável por fazer a leitura dos parâmetros da simulação e executar o simulador.

## Distribuicoes.py

Contém a implementação de diferentes funções para a geração de números aleatórios seguindo uma dada distribuição. Também pode ser utilizado como referência para o arquivo de configuração da simulação, uma vez que os parametros `tecDist` e `tsDist` possuem os mesmos valores dos nomes das funções e os parametros da distribuição selecionada (`tecArgs` e `tsArgs`) são os mesmos da descrita na implementação em notação JSON (mais info olhar `README.md`).

## simulacao.py

Nesse arquivo acontece o processo de simulação propriamente dito. Tempos de Chegada (Tec) e Tempos de Seviços (Ts) são gerados e a partir deles a fila é simulada.
A cada momento, verifica-se qual é o próximo evento (uma chegada ou uma saída). O evento mais próximo é então tratado e calcula-se o seguinte. Isso acontece até que um número previamente definido de clientes seja atendido.

## monteCarlo.py

Nesse arquivo acontece todo o processamento do MMC.
A função geraClasses() divide a base de dados em classes, verifica quantas amostras se encaixam em cada uma delas e calcula qual porcentagem da amostra cada classe detém.
A função geraNumero() usa um valor aleatório entre 0 e 1. Ela verifica em qual intervalo ele se encaixa e retorna o valor associado à respectiva classe.

## Gera_Dados.py

Onde os valores que serão usados como base de dados para o Método Monte Carlo são gerados. 100 números são gerados utilizando a distribuição escolhida.

## estatisticas.py

Esse arquivo é responsável por coletar, processar e apresentar os dados relevantes para a análise da simulação. A cada evento da simulação, o tempo de serviço (ts), tempo de chegada e tempo de saída são armazenados. Ao final, esses dados são exibidos juntamente com outros que são calculados a partir deles.

## Valida.py

Módulo com funções para validação da execução do programa.

## NumeroAleatorio.py

Módulo com função para obter um valor aleatório seguindo a distribuição uniforme no intervalo [0,1].
