# Execução
`python3 escalonamento_(ram,cpu,disco).py < entrada.txt`

## Funcionamento
* Tempo de retorno médio – Refere-se ao tempo transcorrido entre o momento da entrada do processo no sistema e o seu término.
* Tempo de resposta médio – Intervalo de tempo entre a chegada do processo e o início de sua execução.
* Tempo de espera médio – Soma dos períodos em que um processo estava no seu estado pronto.

## CPU

### Entrada

A entrada é composta por uma série de pares de números inteiros separadas por um espaço em branco indicando o instante de chegada do processo e a duração de cada processo.

#### Exemplo de entrada

Instante de chegada | Duração do processo
-- | --
0 | 2
0 | 3
1 | 2
1 | 4

#### Saída
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e os valores das
três métricas solicitadas. Cada linha apresenta a sigla do algoritmo e os valores médios (com
uma casa decimal) para tempo de retorno, tempo de resposta e tempo de espera, exatamente
nesta ordem, separados por um espaço em branco.

#### Exemplo de saída

Algoritmo | Tempo de retorno médio | Tempo de resposta médio | Tempo de espera médio |
-- | -- | -- | -- |
PRI | 7.50 | 1.00 | 4.75 |
LOT | 7.00 | 2.50 | 4.25 |
RR | 6.50 | 2.50 | 3.75 |

## RAM
### Funcionamento:
O programa lê da entrada padrão um conjunto de números inteiros onde o primeiro número representa a quantidade de molduras de página disponíveis na RAM e os demais representam a sequência de referências às páginas, sempre um número por linha.

O programa imprime na saída o número de faltas de páginas obtido com a utilização de cada um dos algoritmos.

### Entrada:
A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória RAM e, em seguida, a sequência de referências à memória.

#### Exemplo de entrada:
4
1
2
3
4
1
2
5
1
2
3
4
5

### Saída
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a utilização de cada um deles.
#### Exemplo de saída:
Algoritmo | Faltas de páginas
-- | --
SC | 7
OTM | 6
CT | 8

## DISCO
### Funcionamento
O programa lê da entrada padrão um conjunto de números inteiros onde o primeiro número representa a quantidade de cilindros no disco, o segundo número representa o cilindro sobre o qual a cabeça de leitura do disco está inicialmente posicionada e os demais representam uma sequência de requisições de acesso a serem atendidas, sempre um número por linha. 

O programa imprime na saída o número total de cilindros percorridos pela cabeça de leitura para atender todas as requisições solicitadas utilizando cada um dos algoritmos.

### Entrada
A entrada é composta por uma série de números inteiros, um por linha, indicando primeiro o número do último cilindro no disco (os cilindros variam de 0 até este número), o cilindro sobre o qual a cabeça de leitura está inicialmente posicionada e a sequência de requisições de acesso.

#### Exemplo de entrada
199
53
98
183
37
122
14
124
65
67

### Saída
A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade total de cilindros percorridos pela cabeça de leitura para atender todas as requisições de acesso ao disco

#### Exemplo de saída

Algoritmo | Quantidade de cilíndros percorridos |
-- | -- |
FCFS | 640 |
SSTF | 236 |
ELEVADOR | 299 |
