
import pygame
from regras_pecas import Regras_pecas

def between(x: float, valor1: float, valor2: float) -> bool:
    # verifica se x esta entre valor1 e valor 2
    if valor1 <= x <= valor2:
        return True
    else:
        return False



class Tabuleiro(Regras_pecas):
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        super().__init__(self.tabuleiro)


    def criar_tabuleiro(self) -> dict[int, list]:
        tabuleiro = {

            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
        }

        x, y = 0, 20  # são os pixels de cada quadrado do tabuleiro

        for i in range(len(tabuleiro)):  # para cada linha em tabuleiro
            for _ in range(
                    8):  # se repete 8 vezes pois esse é o numero de colunas do tabuleiro, é aqui que se define isso
                x += 85  # o primeiro quadrado é criado a 85px da direita, o segundo a 170, e assim por diante ate que se mude a linha, que é determinado por y

                tabuleiro[i].append(
                    [pygame.Rect(x, y, 85, 85), 0, 0])  # cada indice da matriz do tabuleiro recebe uma lista
                # com 3 valores, o quadrado, o valor 0 que representa a inesistencia de peça naquele quadrado e o
                # ultimo 0 que representa que aquele quadrado não existe uma marcação no tabuleiro para indicar aonde a peça pode se mover,
                # caso seja 1 representa que aquele quadrado deve ser verde indicando pra onde a peça pode andar
                # e 2 representa o vermelhor indicando as peças que podem ser capturadas

            y += 85  # y aumenta 85px para que os proximos quadrados sejam criados abaixo dos antigos
            x = 0  # x se reseta para criar a proxima linha

        return tabuleiro


    def desenhar_tabuleiro(self, janela: pygame.Surface) -> None:
        # recebe o tabuleiro com ou sem as peças e desenha ele na tela do pygame

        cores = [
            (64, 43, 35),  # marrom escuro
            (150, 112, 73),  # marrom claro
            (0, 255, 0),
            (255, 0, 0)
        ]
        z = 1  # serve para alternar entre as cores marrom escuro e marrom claro
        for i in self.tabuleiro.values():  # para cada linha em tabuleiro
            for j in i:  # j = cada lista com j[0] = quadrado e j[1] com 0 ou objeto pygame com a imagem da peça
                if j[2] not in [1, 2]:
                    cor = cores[z]
                elif j[2] == 1:
                    cor = cores[2]
                else:
                    cor = cores[3]

                # j[0] == quadrado
                pygame.draw.rect(janela, cor, j[0])

                # j[1][0] == imagens ou o valor 0, isso depende daonde a peça esta posicionada, 0 == nao existe peça aqui
                # j[0][0] == pixels x do quadrado e j[0][1] == pixels y  do quadrado
                # j[2] == objeto pygame com a imagem da marcação
                # so colocarei as peças aonde j[1] != 0, ou seja, aonde existe uma peça

                if j[1] != 0:
                    janela.blit(j[1][0], (j[0][0], j[0][1]))
                elif j[2] != 0:
                    janela.blit(j[2], (j[0][0], j[0][1]))

                # serve para o z ficar alternado a cada loop de 1 a 0, para que haja a troca de cores entre os quadrados do tabueiro
                z = 1 if z == 0 else 0
            z = 1 if z == 0 else 0

    # essa função recebe a posição do clique do mouse
    # e encontra primeiro a coluna aonde se clicou,
    #  exemplo, o primeiro quadrado começa em 85x
    # eu vejo se o x do mouse estar entre o inicio do quadrado em pixels
    # e o final do quadrado que é o inicio dele somado com  o tamanho do quadrado
    # com isso eu encontro a coluna, e depois é so achar a linha verificando somente
    # nos quadrados daquela coluna, desse jeito eu não preciso verificar os 64 quadrados
    def pegar_quadrado_clicado(self, x: int, y: int) -> tuple[int, int]:
        linha = 0
        coluna = 0

        # j = cada quadrado da 1ºlinha, index_coluna = posição dos quadrados da 1ºlinha
        # primeiro eu verifico qual coluna a peça esta
        for index_coluna, j in enumerate(self.tabuleiro[0]):
            # j[0][0] = px de x, j[0][1] = px de y, j[0][2] = dimenções do quadrado
            if between(x, j[0][0], j[0][0] + 85):
                coluna = index_coluna
                break

        # Depois verifico qual a linha que a peça esta
        for index_linha, i in enumerate(self.tabuleiro.values()):
            # i[coluna][quadrado][valor y]
            if between(y, i[coluna][0][1], i[coluna][0][1] + 85):
                linha = index_linha
                break

        return linha, coluna

    def pegar_tabuleiro(self) -> dict[int, list]:
        return self.tabuleiro
