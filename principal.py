import pygame

from tabuleiro.tabuleiro import criar_tabuleiro, desenha_tabuleiro
from pecas.posicionar_pecas import posicionar_pecas

pygame.init()

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Xadrez')

tabuleiro = criar_tabuleiro()

tabuleiro = posicionar_pecas(tabuleiro)
print(tabuleiro)

x = 85
y = 20

rodando = True
while rodando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()


    janela.fill((0, 0, 0))
    desenha_tabuleiro(janela, tabuleiro)
    pygame.display.update()

pygame.quit()
