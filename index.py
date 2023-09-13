print('bem vindo ao jogo da forca')
from wordlwall import palavra
from worldwall import dica
print('boa sorte!')
letras = []
ndechances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra in letras:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    
    print(f'ainda restam {ndechances} chances')
    tentativa = input('escolha uma letra:')
    letras.append(tentativa)
    if tentativa not in palavra:
        ndechances -= 1
    
    ganhou = all(letra in letras for letra in palavra)
    if ganhou:
        print(f'parabéns, você venceu, a palavra era {palavra}')
        break
    elif ndechances == 0:
        break

if not ganhou:
    print(f'que pena, você perdeu, a palavra era {palavra}')
