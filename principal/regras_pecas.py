from typing import List, Tuple, Any

import pygame

pygame.init()


class Regras_pecas:
    def __init__(self, tabuleiro):
        self.tabuleiro = dict(tabuleiro)
        self.marcador = pygame.image.load(
            r"C:\Users\joaol\PycharmProjects\Xadrez\pecasImg\marcacoes_tabuleiro\ponto2.png")

    def _piao(self, linha, coluna, cor: int):  # cor = 0 branco e 1 pra preto
        # é um vetor que faz parte da matrix do xadrex mas seus valores percentem
        # aos quadrados que possuem a linha e a coluna de toda a rota que a peça pode fazer

        caminho = {
            "vetor_caminho": [],
            "vetor_caminho_captura": []
        }

        def piao_preto(l, c):

            # preenchendo vetor de caminho
            if linha == 1:  # caso o pião preto esteja na casa inial ele anda até duas casa
                caminho["vetor_caminho"] = [[l + i, c] for i in range(1, 3) if not self.tem_peca(l + i, c)]
            else:
                caminho["vetor_caminho"] = [[l + 1, c]] if not self.tem_peca(l + 1, c) else []

            # preenchendo vetor de captura piao preto, que preenche as duas primeiras diagonais caso haja peça branca pra capturar

            caminho["vetor_caminho_captura"] = [[l + 1, c - 1 + 2 * (i == 1)] for i in range(2) if
                                                self.tem_peca(l + 1, c - 1 + 2 * (i == 1), 'b')]

        def piao_branco(l, c):
            # preenchendo vetor caminho
            if linha == 6:
                caminho["vetor_caminho"] = [[l - i, c] for i in range(1, 3) if not self.tem_peca(l - 1, c)]
            else:
                caminho["vetor_caminho"] = [[l - 1, c]] if not self.tem_peca(l - 1, c) else []

            # preenchendo vetor de captura, que preenche as duas primeiras diagonais caso haja peça preta pra capturar

            caminho["vetor_caminho_captura"] = [[l - 1, c - 1 + 2 * (i == 1)] for i in range(2) if
                                                self.tem_peca(l - 1, c - 1 + 2 * (i == 1), 'p')]

        if cor == 1:
            piao_preto(linha, coluna)
        else:
            piao_branco(linha, coluna)
        print(caminho)
        return caminho


    def aplicar_regra(self, linha, coluna, peca):
        marcacao = pygame.image.load(r'C:\Users\joaol\PycharmProjects\Xadrez\pecasImg\marcacoes_tabuleiro\ponto2.png')
        if peca == "piao_p":
            x = self._piao(linha, coluna, 1)

            for i in x["vetor_caminho"]:
                if not self.tem_peca(i[0], i[1]):
                    self.tabuleiro[i[0]][i[1]][2] = marcacao

            return x

        elif peca == "piao_b":
            x = self._piao(linha, coluna, 0)
            for i in x["vetor_caminho"]:
                if not self.tem_peca(i[0], i[1]):
                    self.tabuleiro[i[0]][i[1]][2] = marcacao
            return x

    def movimento_valido(self, regra, linha_atual, coluna_atual) -> bool:
        for x in regra["vetor_caminho_captura"]:
            if x[0] == linha_atual and x[1] == coluna_atual:
                return True

        for x in regra["vetor_caminho"]:
            if x[0] == linha_atual and x[1] == coluna_atual:
                return True

        return False

    def remover_regra(self):
        for i in self.tabuleiro.keys():
            for j in range(len(self.tabuleiro[0])):
                self.tabuleiro[i][j][2] = 0

    def tem_peca(self, linha: int, coluna: int, cor=None) -> bool: # cor = b, branco ou p, preto
        if cor is not None:
            if 8 > linha > -1 and 8 > coluna > -1:
                if self.tabuleiro[linha][coluna][1] != 0 and self.tabuleiro[linha][coluna][1][1][-1:] == cor:
                    return True
                else:
                    return False
            else: # caso o valor da linha ou coluna seja maior que 7, ele sai do tabuleiro
                return False

        if 8 > linha > -1 and 8 > coluna > -1:
            if self.tabuleiro[linha][coluna][1] == 0:
                return False
            else:
                return True
        else: # caso o valor da linha ou coluna seja maior que 7, ele sai do tabuleiro
            return False