# Autoria do Código: Márcio Piva
# Comentários: Billy Joe Santos

# Importando bibliotecas necessárias
import sys
import numpy as np
from numpy import random
from typing import Final
import matplotlib.pyplot as plt


# --------------------------
# CONSTANTES DO PROBLEMA
# FRASE: string alvo que queremos "evoluir"
# TAM_CROMO: tamanho de cada cromossomo (igual ao tamanho da frase)
# TAM_POP: tamanho da população (duas vezes o tamanho da frase)
# --------------------------
FRASE: Final[str] = 'EuAdoroInteligenciaArtificialPorqueTemMuitaMatematica'
TAM_CROMO: Final[int] = len(FRASE)
TAM_POP: Final[int] = TAM_CROMO*2


# --------------------------
# ESTRUTURAS DA POPULAÇÃO
# pop: população atual (matriz de inteiros representando caracteres ASCII)
# nova_pop: próxima geração a ser formada
# pais: cromossomos selecionados para reprodução
# filhos: resultado do cruzamento entre pais
# nota_pop: matriz de avaliação da população (id, aptidão, probabilidade)
# --------------------------
pop = np.zeros((TAM_POP, TAM_CROMO))
nova_pop = np.zeros((TAM_POP, TAM_CROMO))
pais = np.zeros((2, TAM_CROMO))
filhos = np.zeros((2, TAM_CROMO))
nota_pop = np.zeros((TAM_POP, 3))


# --------------------------
# Inicializa a população com valores aleatórios (caracteres ASCII de 65 a 122)
# --------------------------
def init_pop():
    global pop
    pop = random.randint(low=65, high=122, size=(TAM_POP, TAM_CROMO))


# --------------------------
# Avalia cada indivíduo da população
# Calcula a "aptidão" (diferença entre o cromossomo e a frase alvo)
# Normaliza os valores para gerar probabilidades de seleção
# --------------------------
def avalia_pop():
    global nota_pop
    soma_apt = 0
    for i in range(TAM_POP):

        apt = 0
        for j in range(TAM_CROMO):
            apt = apt + ((ord(FRASE[j]) - pop[i][j])**2)

        nota_pop[i][0] = i          # índice do indivíduo
        nota_pop[i][1] = apt        # aptidão (quanto menor, melhor)
        nota_pop[i][2] = -1         # probabilidade inicial indefinida
        soma_apt = soma_apt + apt

    # ordena população pelo valor da aptidão
    minsum = 0
    nota_pop = nota_pop[nota_pop[:, 1].argsort()]
    for i in range(TAM_POP):
        if(soma_apt > 0) and (nota_pop[i][1] > 0):
            nota_pop[i][2] = ((1 / nota_pop[i][1]) / soma_apt) * 100
        else:
            nota_pop[i][2] = 0
        minsum = minsum + nota_pop[i][2]

    # normalização final das probabilidades
    for i in range(TAM_POP):
        if(minsum > 0):
            nota_pop[i][2] = nota_pop[i][2] / minsum
        else:
            nota_pop[i][2] = 0


# --------------------------
# Seleciona dois pais por roleta viciada
# Quanto melhor a aptidão, maior a chance de ser escolhido
# --------------------------
def seleciona_pais():
    global pais
    r_pai1 = random.random_sample(size=None)
    r_pai2 = random.random_sample(size=None)

    acum = 0
    for i in range(TAM_POP):
        acum = acum + nota_pop[i][2]
        if(acum >= r_pai1):
            pais[0] = pop[nota_pop[i][0].astype(int)]
            break

    acum = 0
    for i in range(TAM_POP):
        acum = acum + nota_pop[i][2]
        if(acum >= r_pai2):
            pais[1] = pop[nota_pop[i][0].astype(int)]
            break


# --------------------------
# Realiza o cruzamento dos pais
# 80% de chance de cruzar com ponto de corte
# Caso contrário, filhos são cópias dos pais
# --------------------------
def cruza_pais():
    global filhos

    r_cruza = random.random_sample(size=None)
    if(r_cruza < 0.80):
        corte = random.randint(low=0, high=TAM_CROMO-1)
        filhos[0][:corte] = pais[0][:corte]
        filhos[0][corte:] = pais[1][corte:]
        filhos[1][corte:] = pais[0][corte:]
        filhos[1][:corte] = pais[1][:corte]
    else:
        filhos[0] = pais[0]
        filhos[1] = pais[1]


# --------------------------
# Aplica mutação em cada gene com probabilidade de 3%
# Substitui o valor por um caractere ASCII aleatório
# --------------------------
def muta_filhos():
    global filhos

    for i in range(TAM_CROMO):
        r_muta = random.random_sample(size=None)
        if(r_muta < 0.03):
            filhos[0][i] = random.randint(low=65, high=122)

    for i in range(TAM_CROMO):
        r_muta = random.random_sample(size=None)
        if(r_muta < 0.03):
            filhos[1][i] = random.randint(low=65, high=122)


# --------------------------
# Aplica elitismo: preserva os melhores indivíduos na próxima geração
# --------------------------
def elitismo(qtde):
    global nova_pop
    for i in range(qtde):
        nova_pop[i] = pop[nota_pop[i][0].astype(int)]


# --------------------------
# Funções auxiliares para imprimir população e estatísticas
# --------------------------
def imprime_pop():
    for i in range(len(FRASE)*2):
      # Para cada indivíduo, percorre cada gene (caractere)
        for j in range(len(FRASE)):
          # Converte o valor numérico (ASCII) em caractere e imprime sem pular linha
            sys.stdout.write(chr(pop[i][j]))
        # Depois de imprimir todos os genes do indivíduo, pula para a próxima linha
        print("")


def imprime_nota_pop():
    acum = 0
    # Percorre toda a população já avaliada
    for i in range(TAM_POP):
        # acumula a soma das probabilidades para exibir o valor acumulado
        acum = acum + nota_pop[i][2]
        # Mostra índice do indivíduo, nota de aptidão (erro),
        # probabilidade de seleção (%) e valor acumulado da roleta
        print('Individuo: ', nota_pop[i][0], '- Nota: ', nota_pop[i][1], '- (%): ', nota_pop[i][2], ' - Acum: ', acum)


def imprime_melhor():
    # Cabeçalho do melhor indivíduo
    sys.stdout.write('>> Melhor: ')
    # Percorre todos os genes do melhor indivíduo (primeiro da lista ordenada)
    for i in range(len(FRASE)):
        # Acessa o índice do melhor indivíduo: nota_pop[0][0]
        # Converte para inteiro -> int
        # Acessa o cromossomo correspondente em pop
        # Pega o gene i
        # Converte para inteiro (redundante, mas garante tipo)
        # Converte de ASCII para caractere
        # Imprime o caractere sem pular linha
        sys.stdout.write(chr(pop[nota_pop[0][0].astype(int)][i].astype(int)))
    # Ao final, imprime nota de aptidão e probabilidade do melhor indivíduo
    print(' - Nota: ', nota_pop[0][1], ' - (%): ', nota_pop[0][2])


def imprime_pior():
    # Cabeçalho do pior indivíduo
    sys.stdout.write('>> Pior:   ')
    # Percorre todos os genes do pior indivíduo (último da lista ordenada)
    for i in range(len(FRASE)):
        # nota_pop[TAM_POP-1][0] -> índice do pior indivíduo
        # Converte para inteiro -> int
        # Acessa o cromossomo correspondente
        # Pega o gene i
        # Converte para inteiro
        # Converte para caractere ASCII
        # Imprime sem quebra de linha
        sys.stdout.write(chr(pop[nota_pop[TAM_POP-1][0].astype(int)][i].astype(int)))
    # Ao final, imprime nota de aptidão e probabilidade do pior indivíduo
    print(' - Nota: ', nota_pop[TAM_POP-1][1], ' - (%): ', nota_pop[TAM_POP-1][2])


def imprime_medio():
    # Cabeçalho do indivíduo mediano
    sys.stdout.write('>> Medio:  ')
    # Percorre todos os genes do indivíduo do meio da população
    for i in range(len(FRASE)):
        # nota_pop[(TAM_POP - 1)//2][0] -> índice do indivíduo mediano
        # Converte para inteiro -> int
        # Acessa o cromossomo correspondente
        # Pega o gene i
        # Converte para inteiro
        # Converte para caractere ASCII
        # Imprime sem quebra de linha
        sys.stdout.write(chr(pop[nota_pop[((TAM_POP - 1) // 2)][0].astype(int)][i].astype(int)))
    # Ao final, imprime nota de aptidão e probabilidade do indivíduo mediano
    print(' - Nota: ', nota_pop[((TAM_POP - 1) // 2)][1], ' - (%): ', nota_pop[((TAM_POP - 1) // 2)][2])


# --------------------------
# PROGRAMA PRINCIPAL
# 1. Inicializa população
# 2. Avalia, seleciona, cruza, muta e substitui
# 3. Aplica elitismo
# 4. Repete até atingir número máximo de gerações ou solução ótima
# 5. Plota gráficos de convergência
# --------------------------
if(__name__ == '__main__'):
    #listas para graficos
    geracao = []
    melhor = []
    pior = []
    medio = []

    print(FRASE)
    init_pop()
    imprime_pop()

    for i in range(2000):
        print('GERACAO: ', i)
        avalia_pop()

        imprime_melhor()
        imprime_pior()
        imprime_medio()

        #criterio de parada (atingiu a frase alvo)
        if(nota_pop[0][1] < 1):
            break

        #dados para graficos
        geracao.append(i)
        melhor.append(nota_pop[0][1])
        pior.append(nota_pop[TAM_POP-1][1])
        medio.append(nota_pop[(TAM_POP-1)//2][1])

        #preservar n melhores
        j = 4
        elitismo(j)

        #gerar nova populacao por seleção, cruzamento e mutação
        while(j < TAM_POP):
            seleciona_pais()
            cruza_pais()
            muta_filhos()
            nova_pop[j] = filhos[0]
            nova_pop[j+1] = filhos[1]
            j = j + 2

        pop = nova_pop.copy()
        nova_pop = np.zeros((TAM_POP, TAM_CROMO))


    # --------------------------
    # Gráfico de convergência mostrando evolução da aptidão
    # --------------------------
    plt.title("CONVERGENCIA AG")
    plt.plot(geracao, melhor, label = "Melhor")
    plt.plot(geracao, pior, label = "Pior")
    plt.plot(geracao, medio, label = "Medio")
    plt.legend()
    plt.show()

    print('\nRESULTADO FINAL')
    imprime_melhor()
    imprime_pior()
    imprime_medio()