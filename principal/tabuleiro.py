import pygame



class Criar_tabuleiro():
    def criar_tabuleiro(self):
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
                    [pygame.Rect(x, y, 85, 85), 0])  # cada indice da matriz do tabuleiro recebe uma lista
                # com 2 valores, o quadrado e o valor 0 que representa a inesistencia de peça naquele quadrado

            y += 85  # y aumenta 85px para que os proximos quadrados sejam criados abaixo dos antigos
            x = 0  # x se reseta para criar a proxima linha

        return tabuleiro

class Tabuleiro():
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro


    # recebe o tabuleiro com ou sem as peças e desenha ele na tela do pygame
    def desenhar_tabuleiro(self, janela: pygame.Surface):

        cores = [
            (64, 43, 35),  # marrom escuro
            (150, 112, 73)  # marrom claro
        ]
        z = 0  # serve para alternar entre as cores marrom escuro e marrom claro
        for i in self.tabuleiro.values():  # para cada linha em tabuleiro
            for j in i:  # j = cada lista com j[0] = quadrado e j[1] com 0 ou objeto pygame com a imagem da peça
                cor = cores[z]
                # j[0] == quadrado
                pygame.draw.rect(janela, cor, j[0])

                # j[1][0] == imagens ou o valor 0, isso depende daonde a peça esta posicionada, 0 == nao existe peça aqui
                # j[0][0] == pixels x do quadrado e j[0][1] == pixels y  do quadrado
                # so colocarei as peças aonde j[1] != 0, ou seja, aonde existe uma peça

                if j[1] != 0:
                    janela.blit(j[1][0], (j[0][0], j[0][1]))
                # serve para o z ficar alternado a cada loop de 1 a 0, para que haja a troca de cores entre os quadrados do tabueiro
                z = 1 if z == 0 else 0
            z = 1 if z == 0 else 0



