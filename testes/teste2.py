# uso pra testar alguma logica de algo especifico que vem na mente, pra aplicar no principal


def teste1():
    from PIL import Image

    x = Image.open('../pecas/pecas_brancas/rei_b.png')

    nova = x.resize((85, 85))

    nova.save(r'C:\Users\joaol\PycharmProjects\Xadrez\pecas_pretas\nova.png')



def between(x, z, y):
    if z <= x <= y:
        return True
    else:
        return False


print(between())
