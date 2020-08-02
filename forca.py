import random
def imprime_letras_e_undeline(letras,palavra):
    nova_palavra= str()
    contem_letra = False
    for i in range(0,len(palavra)):
        contem_letra = False
        for j in range(0,len(letras)):
            if(letras[j] == palavra[i]):
                nova_palavra =  nova_palavra  + '{} '.format(letras[j])
                contem_letra = True
                break;
        if(not contem_letra):
            if not palavra[i].isalpha():
                nova_palavra = nova_palavra + palavra[i]
            else:
                nova_palavra= nova_palavra + '_ '
    return nova_palavra
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(palavra_secreta):
    print("A palavra era {}".format(palavra_secreta))
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def verifica_se_acertou(letras, palavra):
    qtd_letras =0
    for i in range (0,len(palavra)):
        for j in range(0,len(letras)):
            if(letras[j] == palavra[i]):
                qtd_letras+=1
                break
    if(qtd_letras == len(palavra)):
        return True
    else:
        return False

def return_letras(letras):
    retorno = str()
    for letra in letras:
        retorno = retorno + '{} '.format(letra)
    return retorno

def abertura_de_arquivo():
    filein =  open('palavras.txt', 'r')
    palavras = []
    for linha in filein:
        palavras.append(linha.strip())
    filein.close()
    return sorted(palavras)

def msg_sainda_imput(letras,palavra,enforcou):
    string_principal = "\nquantidade de tentativas {}\n{}\n{}\nqual letra ".format(enforcou,return_letras(letras),imprime_letras_e_undeline(letras,palavra))
    return string_principal

def letra_in_list(cmp_letra,palavra):
    for letra in palavra:
        if cmp_letra == letra:
            return False
    return True

def jogar():
    print('iniciando....')
    palavras = abertura_de_arquivo();
    palavra = palavras[random.randrange(0,len(palavras))]
    print('tudo pronto!')
    palavra = palavra.upper()
    acertou =  True
    enforcou = 7
    letras = list()
    while not verifica_se_acertou(letras,palavra) and enforcou:
        desenha_forca(enforcou)
        letras.append(input(msg_sainda_imput(letras,palavra,enforcou)).upper())
        if letra_in_list(letras[-1],palavra):
            enforcou-=1
        if not enforcou:
            imprime_mensagem_perdedor(palavra)
        else:
            if(verifica_se_acertou(letras,palavra)):
                imprime_mensagem_vencedor(palavra)
    
if(__name__ == '__main__'):
    jogar()