# aqui é aonde eu uso pra testar o que esotu aprendendo sobre o pygame, ja que nunca o ultilizei antes
# isso aqui é uma bagunça!

import pygame

pygame.init()

altura = 600
largura = 1260



quadros = [
    pygame.image.load('../pecas/pecas_pretas/torre_p.png'),
    pygame.image.load('../pecas/pecas_brancas/bispo_b.png')
]
quadro_atual = 0
tempo_quadro = 300
tempo_anterior = pygame.time.get_ticks()



janela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Primeiro Jogo! ")

velocidade = 1
x = 100
y = 50
def teste(janela: pygame.Surface, x, y):
    janela.blit(quadros[1], (x, y))


retangulo1 = pygame.Rect(300, 100, 50, 50)
retangulo2 = pygame.Rect(50, 50, 85, 85)


rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    if pygame.mouse.get_pressed()[0]:
        posicao_mouse = pygame.mouse.get_pos()
        x, y = 50, 50
        retangulo1.move_ip(x, y)


    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - tempo_anterior >= tempo_quadro:
        quadro_atual += 1
        if quadro_atual == len(quadros):
            quadro_atual = 0
        tempo_anterior = pygame.time.get_ticks()

    janela.fill((0, 0, 255))

    janela.blit(quadros[quadro_atual], (300, 50))

    if retangulo1.colliderect(retangulo2):
        print('Colisão detectada')

    #retangulo1[0] = x
    #retangulo1[1] = y
    pygame.draw.rect(janela, (255, 0, 0), retangulo1)
    pygame.draw.rect(janela, (255, 0, 0), retangulo2)

    teste(janela, x, y)

    pygame.display.update()


pygame.quit()

