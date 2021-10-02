# ms-mm1

Simulador mm1

## Alunos

- Gustavo Candido (11711BCC011)
- Mateus Lemos (11811BCC007)

## Dependências

- `python3` instalado na máquina
- `pip3` instalado na máquina
- pacote **tabulate**
  - `pip3 install tabulate`
- pacote **bisect**
  - `pip3 install bisect`

# Instruções de execução

No arquivo `parametros-simulacao` se encontra um JSON contendo os parametros necessários para a execução da simulação. Alguns dos parametros aceitos no arquivo são:

<table>
<tr>
  <th>Nome</th>
  <th style="width: 55%">Descrição</th>
  <th style="width: 55%">Valores Possíveis</th>
</tr>

<tr>
  <td>
    <code>nClientes</code>
  </td>

  <td>
    Número de clientes do sistema
  </td>
  
  <td>
    <code> inteiro > 0</code>
  </td>
</tr>

<tr>
  <td>
    <code>filaMax</code>
  </td>

  <td>
    Tamanho máximo da fila
  </td>
  
  <td>
    <code> inteiro > 0,</code>
    <code> string "inf"</code>
  </td>
</tr>

</table><br>

Além disso também é possível configurar o tipo de distribuição gerada pelos tempos de chegada entre clientes e pelo tempo de serviço e seus respectivos parametros (tecArgs e tsArgs). As distribuições suportadas são:

<table>
<tr>
  <th>Nome da Função</th>
  <th style="width: 55%">Parâmetros</th>
  <th style="width: 55%">Detalhes</th>
</tr>

<tr>
  <td>
    <code>deterministica</code>
  </td>

  <td>
    valor (float)
  </td>

  <td>
    Valor que será utilizado em cada iteração
  </td>
</tr>

<tr>
  <td>
    <code>uniforme</code>
  </td>

  <td>
    min (float) e max (float) 
  </td>
  
  <td>
    Os valores serão gerados no intervalo [min, max]
  </td>
</tr>

<tr>
  <td>
    <code>normal</code>
  </td>

  <td>
    media (float) e desvio (float) 
  </td>
  
  <td>
    Os valores gerados de acordo com a média e o desvio padrão dados
  </td>
</tr>

<tr>
  <td>
    <code>exponencial</code>
  </td>

  <td>
    lamb (float) 
  </td>
  
  <td>
    Os valores serão gerados por uma distribuição exponencial com parâmentro lambda = lamb
  </td>
</tr>

</table><br>

Para se usar uma distribuição específica pode-se utilizar o arquivo `Distribuições.py` como referência para definir o nome da distribuição desejada e passá-la aos parâmetros `tecDist` e `tsDist` sendo que os parametros da função de distribuição selecionada serão os mesmos descritos na assinatura da função no do arquivo de distribuições também na notação JSON. Exemplo:

Em `Distribuicoes.py`

```
  def uniforme(min: float, max: float) -> float:
    ...

  def deterministica(valor:float) -> float:
    ...
```

Em `parametros-simulacao`

```
{
  "nClientes": 15,
  "filaMax": "inf",
  "tecDist": "deterministica", -> mesmo nome da função
  "tecArgs": {
    "valor": 9 -> mesmo parametro da função
  },
  "tsDist": "uniforme",
  "tsArgs": {
    "min": 0,
    "max": 1
  }
}
```

Por fim após a configuração basta rodar o comando `python3 main.py` ou `python main.py` dependendo a configuração do sistema.
