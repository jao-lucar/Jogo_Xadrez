from PIL import Image
from os import listdir
import pygame
from pygame import Surface, SurfaceType


class Pecas_img():
    def __int__(self):
        pass

    def redefinir_tamanho(self, pasta: str) -> None:
        # eu recortei as imagens am 150px por 150px, ja que todas as peças vieram dentro de uma imagem so
        # então eu precisei de diminui-las para 85x85 pra encaixar no tabuleiro
        for nome_imagen in listdir(pasta):
            atual = Image.open(f'{pasta}\{nome_imagen}')
            nova = atual.resize((85, 85))
            nova.save(rf'C:\Users\joaol\PycharmProjects\Xadrez\pecas\{pasta}\{nome_imagen}')

    def carregar_imagens_pecas(self, pasta: str) -> dict[str, Surface | SurfaceType]:
        # carrega as imagens das peças usando o pygame para um dicionario,
        # colocando o nome de cada peça como chave para cada objeto pygame
        pecas = {}
        for peca in listdir(pasta):
            # realizo um fatiamento de string para eliminar os _p.png e os _b.png do nome dos arquivos
            # fazer esse fatiamento me ajuda na hora de posicionar as peças, ja que tanto pra pecas brancas quanto pra pretas, o nome é o mesmo
            pecas[f'{peca[:-6]}'] = pygame.image.load(rf'{pasta}\{peca}')
        return pecas
