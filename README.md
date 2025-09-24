# Fluxograma Detalhado do Algoritmo Genético (Como Implementar)

## 1. Definições iniciais

1. Importar bibliotecas necessárias:

   1. Biblioteca `sys` para imprimir caracteres sem quebra de linha. Exemplo do código: `sys.stdout.write(chr(pop[i][j]))`
   2. Biblioteca `numpy` para manipulação de matrizes e vetores. Exemplo do código: `pop = np.zeros((TAM_POP, TAM_CROMO))`
   3. Biblioteca `numpy.random` para geração de números aleatórios. Exemplo do código: `pop = random.randint(low=65, high=122, size=(TAM_POP, TAM_CROMO))`
   4. Biblioteca `typing.Final` para definir constantes imutáveis. Exemplo do código: `FRASE: Final[str] = 'EuAdoroInteligenciaArtificialPorqueTemMuitaMatematica'`
   5. Biblioteca `matplotlib.pyplot` para gerar gráficos de convergência. Exemplo do código: `plt.plot(geracao, melhor, label = "Melhor")`

## 2. Inicialização da população

1. Criar matriz de zeros com as dimensões do produto do tamanho da população pelo tamanho do cromossomo para a população. Tipo de estrutura: matriz bidimensional de inteiros.
2. Preencher cada posição da matriz com números inteiros aleatórios entre 65 e 122 que representam caracteres ASCII.
3. Inicializar estruturas auxiliares:

   1. nova população, tipo matriz bidimensional de inteiros com dimensões iguais à população.
   2. pais, tipo matriz bidimensional de inteiros com duas linhas e colunas iguais ao tamanho do cromossomo.
   3. filhos, tipo matriz bidimensional de inteiros com duas linhas e colunas iguais ao tamanho do cromossomo.
   4. nota população, tipo matriz bidimensional de números decimais com três colunas: índice do indivíduo, valor de aptidão, probabilidade de seleção.

## 3. Avaliação da população

1. Para cada indivíduo da população:

   1. Inicializar a aptidão do indivíduo como zero.
   2. Para cada gene do indivíduo:

      1. Calcular a diferença entre o valor ASCII do gene e o valor ASCII do caractere correspondente da frase alvo.
      2. Elevar a diferença ao quadrado e adicionar ao valor da aptidão do indivíduo.
   3. Armazenar na nota população: índice do indivíduo, valor da aptidão e valor inicial de probabilidade (-1).
2. Ordenar a nota população em ordem crescente pelo valor da aptidão.
3. Calcular a probabilidade de seleção de cada indivíduo como o inverso do valor da aptidão dividido pela soma total das aptidões multiplicado por 100.
4. Normalizar as probabilidades para que a soma seja igual a 1.

## 4. Seleção de pais

1. Gerar dois números aleatórios entre zero e um para selecionar os pais.
2. Para o primeiro pai:

   1. Percorrer a nota população acumulando probabilidades.
   2. Selecionar o indivíduo cujo acumulado de probabilidade seja maior ou igual ao número aleatório.
   3. Copiar os genes do indivíduo selecionado para a estrutura pais na primeira linha.
3. Repetir o mesmo processo para o segundo pai e copiar os genes para a segunda linha da estrutura pais.

## 5. Cruzamento

1. Gerar um número aleatório entre zero e um.
2. Se o número for menor que 0,8:

   1. Escolher um ponto de corte aleatório entre zero e tamanho do cromossomo menos um.
   2. Para o filho 1:

      1. Copiar genes do pai 1 até o ponto de corte.
      2. Copiar genes do pai 2 a partir do ponto de corte até o final.
   3. Para o filho 2:

      1. Copiar genes do pai 2 até o ponto de corte.
      2. Copiar genes do pai 1 a partir do ponto de corte até o final.
3. Se o número for maior ou igual a 0,8, copiar os pais diretamente para os filhos sem alterações.

## 6. Mutação

1. Para cada gene do filho 1:

   1. Gerar um número aleatório entre zero e um.
   2. Se o número for menor que 0,03, substituir o gene por um número inteiro aleatório entre 65 e 122.
2. Repetir o mesmo procedimento para cada gene do filho 2.

## 7. Elitismo

1. Definir a quantidade de melhores indivíduos a preservar.
2. Para cada um dos melhores indivíduos:

   1. Copiar os genes do indivíduo correspondente da população original para a nova população.

## 8. Impressão de resultados

1. Para cada indivíduo da população:

   1. Converter cada gene de ASCII para caractere.
   2. Imprimir os caracteres como uma string.
2. Para melhor, pior e médio indivíduo:

   1. Identificar o índice correspondente na nota população.
   2. Converter os genes do indivíduo em caracteres e imprimir como string.

## 9. Laço principal de gerações

1. Inicializar listas de números inteiros ou decimais para armazenar estatísticas: gerações, melhor, pior e médio valor de aptidão.
2. Inicializar a população chamando a função de inicialização.
3. Loop até atingir 2000 gerações ou a melhor aptidão ser menor que 1:

   1. Avaliar a população chamando a função de avaliação.
   2. Imprimir melhor, pior e médio indivíduo.
   3. Armazenar valores nas listas de estatísticas.
   4. Aplicar elitismo preservando os melhores indivíduos.
   5. Enquanto a nova população não estiver completa:

      1. Selecionar pais.
      2. Aplicar cruzamento para gerar filhos.
      3. Aplicar mutação nos filhos.
      4. Copiar filhos para a nova população.
   6. Substituir a população antiga pela nova população e reinicializar a nova população com zeros.

## 10. Pós-processamento

1. Gerar gráfico da evolução:

   1. Plotar a evolução do melhor indivíduo por geração.
   2. Plotar a evolução do pior indivíduo por geração.
   3. Plotar a evolução do indivíduo médio por geração.
   4. Adicionar título e legenda ao gráfico.
   5. Exibir o gráfico.
2. Imprimir resultado final com melhor, pior e médio indivíduo convertendo genes para caracteres e exibindo como string.
