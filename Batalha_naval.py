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

#afundados

def afundados(frota, tabuleiro):
    afundados = 0
    for tipo, embarcacoes in frota.items():
        for embarcacao in embarcacoes:
            afundado = True
            for posicao in embarcacao:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundado = False
            if afundado:
                afundados += 1
    return afundados

# Posição Válida

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    passarinho = define_posicoes(linha, coluna, orientacao, tamanho)

    for passaro in passarinho:
        if passaro[0]<0 or passaro[0]>9:
            return False
        if passaro[1]<0 or passaro[1]>9:
            return False
    
    for f1 in frota:
        for f2 in frota[f1]:
            for f3 in f2:
                if f3 in passarinho:
                        return False
    return True

# define a frota e as variáveis
frota = {
"porta-aviões":[],
"navio-tanque":[],
"contratorpedeiro":[],
"submarino": [],
}

quantidade_navios = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}

tamanho_navios = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
}

# posicionando frota:

for navio, quantidade in quantidade_navios.items():
    for i in range(quantidade):
        valida = False
        while valida == False:
            print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho_navios[navio]}')
            linha = int(input('linha'))
            coluna = int(input('coluna'))
            if navio != "submarino":
                orientacao = int(input('orientação'))
                if orientacao == 1:
                    orientacao = 'vertical'
                else: 
                    orientacao = 'horizontal'
            else:
                orientacao = 'vertical'
            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho_navios[navio])
            if valida == False:
                print('Esta posição não está válida!')
            else:
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho_navios[navio])   
print(frota)

# O jogo
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

jogando = True
import random 
random.seed(2)
PosicoesAnteriores = []
PosicoesAnterioresOponente = []
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    
    #Tabuleiro
    tabuleiro = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print (tabuleiro)

    # Ataque
    repetir = True
    while repetir:
        Linha = int(input('Em qual linha deseja atacar? '))
        while Linha <0 or Linha >9:
            print ('Linha inválida!')
            Linha = int(input('Em qual linha deseja atacar? '))

        Coluna = int(input('Em qual coluna deseja atacar? '))
        while Coluna <0 or Coluna >9:
            print ('Coluna inválida!')
            Coluna = int(input('Em qual coluna deseja atacar? '))
        if [Linha,Coluna] not in PosicoesAnteriores:
            PosicoesAnteriores.append([Linha, Coluna])
            repetir = False
        
        else:
            print (f'A posição linha {Linha} e coluna {Coluna} já foi informada anteriormente') 

    tabuleiro_oponente =  faz_jogada (tabuleiro_oponente, Linha, Coluna)
    Afundados_jogador = afundados(frota_oponente, tabuleiro_oponente)
    if Afundados_jogador == 10:
        print ('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else: 
        repetir = True
        while repetir: 
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if [linha,coluna] not in PosicoesAnterioresOponente:
                PosicoesAnterioresOponente.append([linha, coluna])
                repetir = False
        print(f'Seu oponente está atacando na linha {linha} e coluna {coluna}')
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador,linha,coluna)
        afundados_oponente = afundados(frota,tabuleiro_jogador)
        if Afundados_oponente == 10:
            print ('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False

            