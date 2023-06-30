import pygame

pygame.init()


class Regras_pecas:
    def __init__(self, tabuleiro):
        self.tabuleiro = dict(tabuleiro)
        self.marcador = pygame.image.load(
            r"C:\Users\joaol\PycharmProjects\Xadrez\pecasImg\marcacoes_tabuleiro\ponto2.png")

        self.caminhos = {
            "vetor_caminho": [],
            "vetor_caminho_captura": []
        }

    def _piao(self, linha, coluna, cor: int):  # cor = 0 branco e 1 pra preto
        # é um vetor que faz parte da matrix do xadrex mas seus valores percentem
        # aos quadrados que possuem a linha e a coluna de toda a rota que a peça pode fazer

        def piao_preto(l, c):

            # preenchendo vetor de caminho
            if self.tem_peca(l + 1, c):
                self.caminhos["vetor_caminho"] = []
            else:
                if linha == 1:  # caso o pião preto esteja na casa inical ele anda até duas casa
                    self.caminhos["vetor_caminho"] = [[l + i, c] for i in range(1, 3)]
                else:
                    self.caminhos["vetor_caminho"] = [[l + 1, c]]

            # preenchendo vetor de captura piao preto, que preenche as duas primeiras diagonais caso haja peça branca pra capturar

            self.caminhos["vetor_caminho_captura"] = [[l + 1, c - 1 + 2 * (i == 1)] for i in range(2) if
                                                      self.tem_peca(l + 1, c - 1 + 2 * (i == 1), 'b')]

        def piao_branco(l, c):
            # preenchendo vetor caminho
            if self.tem_peca(l - 1, c):
                self.caminhos["vetor_caminho"] = []
            else:
                if linha == 6:
                    self.caminhos["vetor_caminho"] = [[l - i, c] for i in range(1, 3)]
                else:
                    self.caminhos["vetor_caminho"] = [[l - 1, c]]

            # preenchendo vetor de captura, que preenche as duas primeiras diagonais caso haja peça preta pra capturar

            self.caminhos["vetor_caminho_captura"] = [[l - 1, c - 1 + 2 * (i == 1)] for i in range(2) if
                                                      self.tem_peca(l - 1, c - 1 + 2 * (i == 1), 'p')]

        if cor == 1:
            piao_preto(linha, coluna)
        else:
            piao_branco(linha, coluna)

    def _bispo(self, linha, coluna, cor):
        self._caminhos_diagonais(linha, coluna, cor)

    def _torre(self, linha, coluna, cor):
        self._caminhos_retos(linha, coluna, cor)

    def _rainha(self, linha, coluna, cor):
        self._caminhos_retos(linha, coluna, cor)
        self._caminhos_diagonais(linha, coluna, cor)

    def _cavalo(self, linha, coluna, cor):
        for i in ([-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]):
            if not self.tem_peca(linha + i[0], coluna + i[1], 1 if cor == 0 else 1):
                self.caminhos["vetor_caminho"].append([linha + i[0], coluna + i[1]])



    def _caminhos_retos(self, l, c, cor):
        l_auxiliar = l
        c_auxiliar = c
        if not self.tem_peca(l, c + 1, 1 if cor == 0 else 1):  # direita
            while True:
                c_auxiliar += 1
                self.caminhos["vetor_caminho"].append([l, c_auxiliar])
                if c_auxiliar == 7 or self.tem_peca(l_auxiliar, c_auxiliar):
                    break
        if not self.tem_peca(l, c - 1, 1 if cor == 0 else 1):  # esquerdo
            c_auxiliar = c
            while True:
                c_auxiliar -= 1
                self.caminhos["vetor_caminho"].append([l, c_auxiliar])
                if c_auxiliar == 0 or self.tem_peca(l, c_auxiliar):
                    break
        if not self.tem_peca(l - 1, c, 1 if cor == 0 else 1):  # cima
            while True:
                l_auxiliar -= 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c])
                if l_auxiliar == 0 or self.tem_peca(l_auxiliar, c):
                    break
        if not self.tem_peca(l + 1, c, 1 if cor == 0 else 1):  # baixo
            l_auxiliar = l
            while True:
                l_auxiliar += 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c])
                if l_auxiliar == 7 or self.tem_peca(l_auxiliar, c):
                    break
    def _caminhos_diagonais(self, l, c, cor):
        # preenchendo o vetor_caminho
        l_auxiliar = l
        c_auxiliar = c
        if not self.tem_peca(l + 1, c + 1, 1 if cor == 0 else 1):  # direira baixo
            l_auxiliar = l
            c_auxiliar = c
            while True:  # enquanto os valores das linhas e colunas estiverem dentro das dimenções do tabuleiro, repita o loop
                l_auxiliar += 1
                c_auxiliar += 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c_auxiliar])
                if l_auxiliar == 7 or c_auxiliar == 7 \
                        or self.tem_peca(l_auxiliar, c_auxiliar):
                    break
        if not self.tem_peca(l + 1, c - 1, 1 if cor == 0 else 1):  # esquerda baixo
            l_auxiliar = l
            c_auxiliar = c
            while True:
                l_auxiliar += 1
                c_auxiliar -= 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c_auxiliar])
                if l_auxiliar == 7 or c_auxiliar == 7 or \
                        c_auxiliar == 0 or self.tem_peca(l_auxiliar, c_auxiliar):
                    break
        if not self.tem_peca(l - 1, c - 1, 1 if cor == 0 else 1):  # esquerda cima
            l_auxiliar = l
            c_auxiliar = c
            while True:
                l_auxiliar -= 1
                c_auxiliar -= 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c_auxiliar])
                if l_auxiliar == 7 or c_auxiliar == 7 or \
                        l_auxiliar == 0 or c_auxiliar == 0 or \
                        self.tem_peca(l_auxiliar, c_auxiliar):
                    break
        if not self.tem_peca(l - 1, c + 1, 1 if cor == 0 else 1):  # direira cima
            l_auxiliar = l
            c_auxiliar = c
            while True:
                l_auxiliar -= 1
                c_auxiliar += 1
                self.caminhos["vetor_caminho"].append([l_auxiliar, c_auxiliar])
                if l_auxiliar == 7 or c_auxiliar == 7 or \
                        l_auxiliar == 0 or self.tem_peca(l_auxiliar, c_auxiliar):
                    break

    def aplicar_regra(self, linha, coluna, peca, cor):
        # essa função serve para adicionar os pontos de referencia(marcação) aonde as peças podem se mover
        # limpa os caminhos a cada peça clicada
        self.caminhos["vetor_caminho"] = []
        self.caminhos["vetor_caminho_captura"] = []

        if peca == "piao_p" or peca == "piao_b":
            self._piao(linha, coluna, cor)
            for i in self.caminhos["vetor_caminho"]:  # i[0] = linha i[1] = coluna
                if not self.tem_peca(i[0], i[1]):
                    self.tabuleiro[i[0]][i[1]][2] = self.marcador
            return

        elif peca == "bispo_b" or peca == "bispo_p":
            self._bispo(linha, coluna, cor)

        elif peca == "torre_b" or peca == "torre_p":
            self._torre(linha, coluna, cor)

        elif peca == "rainha_b" or peca == "rainha_p":
            self._rainha(linha, coluna, cor)

        elif peca == "cavalo_b" or peca == "cavalo_p":
            self._cavalo(linha, coluna, cor)

        for i in self.caminhos["vetor_caminho"]:
            self.tabuleiro[i[0]][i[1]][2] = self.marcador


    def movimento_valido(self, linha_atual, coluna_atual) -> bool:

        for x in self.caminhos["vetor_caminho_captura"]:
            if x[0] == linha_atual and x[1] == coluna_atual:
                return True

        for x in self.caminhos["vetor_caminho"]:
            if x[0] == linha_atual and x[1] == coluna_atual:
                return True

        return False

    def remover_regra(self):
        for i in self.tabuleiro.keys():
            for j in range(len(self.tabuleiro[0])):
                self.tabuleiro[i][j][2] = 0

    def tem_peca(self, linha: int, coluna: int, cor=None) -> bool:  # cor = b, branco ou p, preto
        if cor is not None:
            if 8 > linha > -1 and 8 > coluna > -1:
                if self.tabuleiro[linha][coluna][1] != 0 and self.tabuleiro[linha][coluna][1][1][-1:] == cor:
                    return True
                else:
                    return False
            else:  # caso o valor da linha ou coluna seja maior que 7, ele sai do tabuleiro entao considere como se
                # tivesse uma peça para bloquear esse caminho que nao existe, evitando o erro: index out of range
                return True

        if 8 > linha > -1 and 8 > coluna > -1:
            if self.tabuleiro[linha][coluna][1] == 0:
                return False
            else:
                return True
        else:  # caso o valor da linha ou coluna seja maior que 7, ele sai do tabuleiro
            return True  # caso o valor da linha ou coluna seja maior que 7, ele sai do tabuleiro entao considere como se
            # tivesse uma peça para bloquear esse caminho que nao existe, evitando o erro: index out of range
