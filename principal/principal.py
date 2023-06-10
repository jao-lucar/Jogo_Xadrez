import pygame
from pecas.pecas_img import Pecas_img
from jogo import Jogo

pygame.init()
jogo = Jogo()

pecas_img = Pecas_img()
pecas_p = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_pretas')
pecas_b = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_brancas')

jogo.posicionar_pecas_iniciais(pecas_p, pecas_b)

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Xadrez')

peca_clicada1 = False
peca_clicada2 = False
vezes_clicado = 0
rodando = True

while rodando:
    for e in pygame.event.get():
        # logica para realizar ações do jogo atravez do clique do mouse
        if e.type == pygame.MOUSEBUTTONDOWN:
            vezes_clicado += 1
            pos = pygame.mouse.get_pos()
            linha_atual, coluna_atual = jogo.pegar_quadrado_clicado(pos[0], pos[1])

            # logica para capturar peça
            if vezes_clicado == 2 and peca_clicada1 and jogo.tem_peca(linha_atual, coluna_atual):
                vezes_clicado = 0
                peca_clicada2 = jogo.pegar_peca(linha_atual, coluna_atual)

                if peca_clicada1[1][-1:] != peca_clicada2[1][-1:]:# peca_clicada1[1][-1:] == b ou p, de preto ou branco
                    #esse metodo ja remove a peça aonde a atual esta sendo posicionada, a logica é uma troca entre os objetos dentro da matriz do xadrez
                    jogo.mover_peca(linha_atual, coluna_atual, linha_peca_clicada1,
                                    coluna_peca_clicada1, peca_clicada1)

            elif vezes_clicado == 2:
                vezes_clicado = 0
            #preenche a peca_clicada1
            if jogo.tem_peca(linha_atual, coluna_atual):
                linha_peca_clicada1, coluna_peca_clicada1 = jogo.pegar_quadrado_clicado(pos[0], pos[1])
                peca_clicada1 = jogo.pegar_peca(linha_atual, coluna_atual)
            #logica para mover a peça
            elif peca_clicada1:

                jogo.mover_peca(linha_atual, coluna_atual, linha_peca_clicada1, coluna_peca_clicada1, peca_clicada1)
                peca_clicada1 = False


        if e.type == pygame.QUIT:
            pygame.quit()

    janela.fill((0, 0, 0))
    jogo.desenhar_tabuleiro(janela)
    pygame.display.update()

pygame.quit()
