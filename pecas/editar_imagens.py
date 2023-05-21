from PIL import Image
from os import listdir

# eu recortei as imagens am 150px por 150px, ja que todas as peças vieram dentro de uma imagem so
# então eu precisei de diminui-las para 85x85 pra encaixar no tabuleiro
def redefinir_tamanho(pasta):
    for nome_imagen in listdir(pasta):
        atual = Image.open(f'{pasta}\{nome_imagen}')
        nova = atual.resize((85, 85))
        nova.save(rf'C:\Users\joaol\PycharmProjects\Xadrez\pecas\{pasta}\{nome_imagen}')

redefinir_tamanho('pecas_brancas')
redefinir_tamanho('pecas_pretas')