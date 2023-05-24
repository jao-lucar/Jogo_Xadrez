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
peca_clicada = False
print(pecas_p)


print(tabuleiro_principal)

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Xadrez')


rodando = True
while rodando:
    for e in pygame.event.get():
        #logica para movimentar as peças atravez do clique do mouse
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            linha, coluna = tabuleiro.pegar_quadrado_clicado(pos[0], pos[1])

            if tabuleiro.tem_peca(linha, coluna):
                linha_peca_clicada, coluna_peca_clicada = tabuleiro.pegar_quadrado_clicado(pos[0], pos[1])
                peca_clicada = peca.pegar_peca(linha, coluna, tabuleiro_principal)

            else:

                if peca_clicada:
                    tabuleiro_principal = peca.remover_peca(linha_peca_clicada, coluna_peca_clicada, tabuleiro_principal)
                    tabuleiro_principal = peca.mover_peca(linha, coluna, peca_clicada, tabuleiro_principal)
                    peca_clicada = False

        if e.type == pygame.QUIT:
            pygame.quit()


    janela.fill((0, 0, 0))
    tabuleiro.desenhar_tabuleiro(janela)
    pygame.display.update()

pygame.quit()
