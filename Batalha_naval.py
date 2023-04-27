# Define posições 
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao_ocupada = []
    i = 0
    while i < tamanho:
        if orientacao == 'vertical':
            posicao_ocupada.append([linha+i,coluna]) 
            i+=1
        else:
            posicao_ocupada.append([linha,coluna+i])
            i+=1
    return posicao_ocupada


# Prenchee Frota
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_ocupada = []
    i = 0
    while i < tamanho:
        if orientacao == 'vertical':
            posicao_ocupada.append([linha+i,coluna]) 
            i+=1
        else:
            posicao_ocupada.append([linha,coluna+i])
            i+=1
    if nome_navio in frota:
        frota[nome_navio].append(posicao_ocupada)
    else:
        frota[nome_navio] = [posicao_ocupada]
    return frota


# Faz Jogada
def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro [linha][coluna] == 1:
        tabuleiro [linha][coluna] = 'X'
    else:
        tabuleiro [linha][coluna] = '-'
    return tabuleiro

#Posiciona Frota

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for x in frota:
        for listona in frota[x]:
            for supreme in listona:
                i = supreme[0]
                j = supreme[1]
                tabuleiro[i][j] = 1
    return tabuleiro
a