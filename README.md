# Projeto-2-Dessoft
EP 2
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




# Faz Jogada

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro [linha][coluna] == 1:
        tabuleiro [linha][coluna] = 'X'
    else:
        tabuleiro [linha][coluna] = '-'
    return tabuleiro
