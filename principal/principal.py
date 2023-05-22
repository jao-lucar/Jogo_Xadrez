import pygame
from tabuleiro import Tabuleiro, Criar_tabuleiro
from pecas.pecas_img import Pecas_img
from peca import Peca


criador = Criar_tabuleiro()
tabuleiro_inicial = criador.criar_tabuleiro()
tabuleiro = Tabuleiro(tabuleiro_inicial)

pecas_img = Pecas_img()
pecas_p = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_pretas')
pecas_b = pecas_img.carregar_imagens_pecas(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas\pecas_brancas')

peca = Peca()
peca.posicionar_pecas_iniciais(pecas_p, pecas_b, tabuleiro_inicial)
print(pecas_p)


print(tabuleiro_inicial)





pygame.init()

altura = 720
largura = 900
janela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Xadrez')





"""
for i in t.values():
    for j in i:
        print(j, end='\t\t')
    print()
"""
x = 85
y = 20

rodando = True
while rodando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    teclas = pygame.key.get_pressed()



    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        a = tabuleiro.pegar_quadrado_clicado(pos[0], pos[1])
        print(a)

    janela.fill((0, 0, 0))
    tabuleiro.desenhar_tabuleiro(janela)
    pygame.display.update()

pygame.quit()
