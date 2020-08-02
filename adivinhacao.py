import random
def jogar():
    print('bem vindo!\n')

    numero_secreto = int(random.random()*100)
    tentantivas = 6
    for _ in range (0, tentantivas):
        chute = int(input("Digite seu numero entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print('valor invalido')
            continue
        print('voce digiou, ', chute)
        print('verdadeiro' if chute == numero_secreto else 'errou')
        if(chute == numero_secreto):
            break
    print('o numero era : {}'.format(numero_secreto))
    print('ganhou' if chute == numero_secreto else 'perdeu')

if(__name__ == '__main__'):
    jogar()