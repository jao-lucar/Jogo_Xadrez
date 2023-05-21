import pygame
from os import listdir
pygame.init()


# carrega as imagens das peças usando o pygame para um dicionario,
# colocando o nome de cada peça como chave para cada objeto pygame
def carregar_imagens(pasta):
    pecas = {}
    for peca in listdir(pasta):
        # realizo um fatiamento de string para eliminar os _p.png e os _b.png do nome dos arquivos
        # fazer esse fatiamento me ajuda na hora de posicionar as peças, ja que tanto pra pecas brancas quanto pra pretas, o nome é o mesmo
        pecas[f'{peca[:-6]}'] = pygame.image.load(rf'{pasta}\{peca}')
    return pecas

# as peças sao separadas entre esses 2 dicionários
pecas_p = carregar_imagens('pecas\pecas_pretas')
pecas_b = carregar_imagens('pecas\pecas_brancas')



# essa função faz uma conexão entre os quadrados do tabuleiro e as peças,
# tabuleiro = {0: [quadrado(px), peça(px) ou 0]}, 0=quadrado vazio(sem peça)
def posicionar_pecas(tabuleiro):
    # o fato de eu ter feito um fatiamento de string nos nomes das pastas, me ajuda aqui,
    # ja que eu uso uma lista de ordem_pecas para ambas as peças, pretas e brancas
    ordem_pecas = [['torre', 'cavalo', 'bispo'], ['rei', 'rainha'], ['piao']]

    # essa lista pecas, me ajuda a ultilizar os if e elses abaixo para ambas as peças, pretas e brancas
    #a variavel x que alterna entre pecas[0] = pecas_p e pecas[1] = pecas_b
    pecas = [pecas_p, pecas_b]
    # a variavel k e z, nos ajuda a percorrer a lista ordem-pecas
    x, k, z = 0, 0, 1
    #são as linhas que as peças começam ao iniciar o jogo
    linhas = [0, 1, 6, 7]

    for i in linhas:
        if i == 7:
            #reseta as variaveis menos o x que vai pra 1, pois representa pecas[1], que são as peças brancas
            x, k, z = 1, 0, 1
        for j in range(len(tabuleiro[i])):

            if i == 0 or i == 7:
                # adiciona a torre, cavalo e bispo
                if j <= 2:
                    tabuleiro[i][j][1] = pecas[x][ordem_pecas[0][j]]
                # adiciona o rei e a rainha
                elif j <= 4:
                    tabuleiro[i][j][1] = pecas[x][ordem_pecas[1][k]]
                    k += 1
                # adiciona a torre, cavalo e bispo na ordem contrária
                else:
                    tabuleiro[i][j][1] = pecas[x][ordem_pecas[0][-z]]
                    z += 1

            #adiciona os piões pretos
            if i == 1:
                tabuleiro[i][j][1] = pecas_p[ordem_pecas[2][0]]
            #adiciona os piões brancos
            elif i == 6:
                tabuleiro[i][j][1] = pecas_b[ordem_pecas[2][0]]

    return tabuleiro



