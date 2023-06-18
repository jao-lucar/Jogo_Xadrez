
import pygame
from tabuleiro import Tabuleiro

class Jogo(Tabuleiro):
    def __init__(self):
        super().__init__()

        self.tabuleiro = Tabuleiro().pegar_tabuleiro()

    def posicionar_pecas_iniciais(self, imgs_pecas_p, imgs_pecas_b) -> None:
        # essa função faz uma conexão entre os quadrados do tabuleiro e as peças,
        # tabuleiro = {0: [quadrado(px), peça(px) ou 0]}, 0=quadrado vazio(sem peça)
        # no lugar do 0, colocarei uma lista com o objeto pygame com a imagem, e o nome da peça juntamente com sufixo
        # _p para pretas e _b para brancas
        sufixo = ['_p', '_b']

        # o fato de eu ter feito um fatiamento de string nos nomes das pastas, me ajuda aqui,
        # ja que eu uso uma lista de ordem_pecas para ambas as peças, pretas e brancas
        ordem_pecas = [['torre', 'cavalo', 'bispo'], ['rei', 'rainha'], ['piao']]

        # essa lista pecas, me ajuda a ultilizar os if e elses abaixo para ambas as peças, pretas e brancas
        # a variavel x que alterna entre pecas[0] = pecas_p e pecas[1] = pecas_b
        pecas = [imgs_pecas_p, imgs_pecas_b]
        # a variavel k e z, nos ajuda a percorrer a lista ordem-pecas
        x, k, z = 0, 0, 1
        # são as linhas que as peças começam ao iniciar o jogo
        linhas = [0, 1, 6, 7]

        for i in linhas:
            if i == 7:
                # reseta as variaveis menos o x que vai pra 1, pois representa pecas[1], que são as peças brancas
                x, k, z = 1, 0, 1
            for j in range(len(self.tabuleiro[i])):

                if i == 0 or i == 7:
                    # adiciona a torre, cavalo e bispo
                    if j <= 2:
                        self.tabuleiro[i][j][1] = [pecas[x][ordem_pecas[0][j]], f"{ordem_pecas[0][j]}{sufixo[x]}"]
                    # adiciona o rei e a rainha
                    elif j <= 4:
                        self.tabuleiro[i][j][1] = [pecas[x][ordem_pecas[1][k]], f"{ordem_pecas[1][k]}{sufixo[x]}"]
                        k += 1
                    # adiciona a torre, cavalo e bispo na ordem contrária
                    else:
                        self.tabuleiro[i][j][1] = [pecas[x][ordem_pecas[0][-z]], f"{ordem_pecas[0][-z]}{sufixo[x]}"]
                        z += 1

                # adiciona os piões pretos
                if i == 1:
                    self.tabuleiro[i][j][1] = [imgs_pecas_p[ordem_pecas[2][0]], f"{ordem_pecas[2][0]}{sufixo[0]}"]
                # adiciona os piões brancos
                elif i == 6:
                    self.tabuleiro[i][j][1] = [imgs_pecas_b[ordem_pecas[2][0]], f"{ordem_pecas[2][0]}{sufixo[1]}"]

    def posicionar_1peca(self, img_peca, cor) -> None:
        self.tabuleiro[6][4][1] = [img_peca, f"piao_{cor}"]



    def pegar_peca(self, linha: int, coluna: int) -> list:
        return self.tabuleiro[linha][coluna][1] if self.tabuleiro[linha][coluna][1] != 0 else None

    def remover_peca(self, linha: int, coluna: int) -> None:
        self.tabuleiro[linha][coluna][1] = 0

    def mover_peca(self, nova_linha: int, nova_coluna: int,
                   antiga_linha: int, antiga_coluna: int, peca: pygame.surface) -> None:

        self.tabuleiro[nova_linha][nova_coluna][1] = peca
        self.remover_peca(antiga_linha, antiga_coluna)

