import pygame
from pecasImg.pecas_img import Pecas_img
from jogo import Jogo

pygame.init()
jogo = Jogo()

pecas_img = Pecas_img()
pecas_p = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecasImg\pecas_pretas')
pecas_b = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecasImg\pecas_brancas')

jogo.posicionar_pecas_iniciais(pecas_p, pecas_b)

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Xadrez')

peca_clicada1 = False
linha_peca_clicada1 = False
coluna_peca_clicada1 = False
regra = False
vezes_clicado = 0
rodando = True
alternador = {
    0: "b",
    1: "p"
}
alterna = 0
while rodando:
    for e in pygame.event.get():
        # logica para realizar ações do jogo atravez do clique do mouse
        if e.type == pygame.MOUSEBUTTONDOWN:

            vezes_clicado += 1
            pos = pygame.mouse.get_pos()
            linha_atual, coluna_atual = jogo.pegar_quadrado_clicado(pos[0], pos[1])

            # faz com que se o jogador clicar em um espeço em branco o codigo reseta o loop, faz com que o codigo continue apenas se uma peça for clicada
            if vezes_clicado == 1:
                # preenche a peca_clicada1
                if jogo.tem_peca(linha_atual, coluna_atual, alternador[alterna]):
                    peca = jogo.pegar_peca(linha_atual, coluna_atual)
                    linha_peca_clicada1, coluna_peca_clicada1 = jogo.pegar_quadrado_clicado(pos[0], pos[1])
                    peca_clicada1 = jogo.pegar_peca(linha_atual, coluna_atual)
                    regra = jogo.aplicar_regra(linha_atual, coluna_atual, peca_clicada1[1])
                else:
                    jogo.remover_regra()
                    vezes_clicado = 0
                    break
            elif vezes_clicado == 2:
                # logica para capturar peça
                if jogo.tem_peca(linha_atual, coluna_atual, alternador[1 if alterna == 0 else 0]) \
                                and jogo.movimento_valido(regra, linha_atual, coluna_atual):

                    # esse metodo ja remove a peça aonde a atual esta sendo posicionada, a logica é uma troca entre os objetos dentro da matriz do xadrez
                    jogo.mover_peca(linha_atual, coluna_atual, linha_peca_clicada1,
                                    coluna_peca_clicada1, peca_clicada1)
                    jogo.remover_regra()
                    alterna = 1 if alterna == 0 else 0
                    vezes_clicado = 0
                    break
                elif jogo.movimento_valido(regra, linha_atual, coluna_atual):
                    jogo.mover_peca(linha_atual, coluna_atual, linha_peca_clicada1, coluna_peca_clicada1, peca_clicada1)
                    jogo.remover_regra()
                    alterna = 1 if alterna == 0 else 0
                    vezes_clicado = 0
                    break
                else:
                    jogo.remover_regra()
                    vezes_clicado = 0
                    break

        if e.type == pygame.QUIT:
            pygame.quit()

    janela.fill((0, 0, 0))
    jogo.desenhar_tabuleiro(janela)
    pygame.display.update()

pygame.quit()
