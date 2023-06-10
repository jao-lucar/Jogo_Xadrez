import pygame
from tabuleiro import Tabuleiro, Criar_tabuleiro
from pecas.pecas_img import Pecas_img
from peca import Peca

pygame.init()

criador = Criar_tabuleiro()
tabuleiro_principal = criador.criar_tabuleiro()
tabuleiro = Tabuleiro(tabuleiro_principal)

pecas_img = Pecas_img()
pecas_p = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_pretas')
pecas_b = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_brancas')

peca = Peca()
peca.posicionar_pecas_iniciais(pecas_p, pecas_b, tabuleiro_principal)
peca_clicada1 = False
peca_clicada2 = False
print(pecas_p)

print(tabuleiro_principal)

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Xadrez')
vezes_clicado = 0
rodando = True
while rodando:
    for e in pygame.event.get():
        # logica para movimentar as peças atravez do clique
        if e.type == pygame.MOUSEBUTTONDOWN:
            vezes_clicado += 1
            pos = pygame.mouse.get_pos()
            linha, coluna = tabuleiro.pegar_quadrado_clicado(pos[0], pos[1])
            # logica para capturar peça
            if vezes_clicado == 2 and peca_clicada1 and tabuleiro.tem_peca(linha, coluna):
                vezes_clicado = 0
                peca_clicada2 = peca.pegar_peca(linha, coluna, tabuleiro_principal)

                if peca_clicada1[1][-1:] != peca_clicada2[1][-1:]:# peca_clicada1[1][-1:] = b ou p, de preto ou branco
                    tabuleiro_principal = peca.remover_peca(linha, coluna, tabuleiro_principal)
                    tabuleiro_principal = peca.remover_peca(linha_peca_clicada1, coluna_peca_clicada1, tabuleiro_principal)
                    tabuleiro_principal = peca.mover_peca(linha, coluna, peca_clicada1, tabuleiro_principal)

            elif vezes_clicado == 2:
                vezes_clicado = 0

            if tabuleiro.tem_peca(linha, coluna):
                linha_peca_clicada1, coluna_peca_clicada1 = tabuleiro.pegar_quadrado_clicado(pos[0], pos[1])
                peca_clicada1 = peca.pegar_peca(linha, coluna, tabuleiro_principal)
            #logica para mover a peça
            elif peca_clicada1:
                tabuleiro_principal = peca.remover_peca(linha_peca_clicada1, coluna_peca_clicada1, tabuleiro_principal)
                tabuleiro_principal = peca.mover_peca(linha, coluna, peca_clicada1, tabuleiro_principal)
                peca_clicada1 = False





        if e.type == pygame.QUIT:
            pygame.quit()

    janela.fill((0, 0, 0))
    tabuleiro.desenhar_tabuleiro(janela)
    pygame.display.update()

pygame.quit()
