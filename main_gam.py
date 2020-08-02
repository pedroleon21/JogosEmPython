import adivinhacao
import forca
jogando = True
while jogando:
    print('1. foca\n2. adivinhacao')
    escolha = int(input('qual jogo: '))
    if(escolha == 1):
        forca.jogar()
    if(escolha == 2):
        adivinhacao.jogar()
    if( input("deseja continar jogando? \n1.S\n2.N ").upper() == 'N'):
        jogando = False
    else:
        jogando = True