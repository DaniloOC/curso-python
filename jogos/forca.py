import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        index = 0
        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, letras_acertadas, chute, index)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_acertou()
    else:
        imprime_mensagem_enforcou(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    POSTE = " |            "

    if(erros > 4):
        print(" |      \|/   ")

    if(erros > 5):
        print(" |       |    ")

    if(erros == 1):
        print(POSTE)
        print(POSTE)
        print(POSTE)

    if(erros == 2):
        print(" |      \     ")
        print(POSTE)
        print(POSTE)

    if(erros == 3):
        print(" |      \|    ")
        print(POSTE)
        print(POSTE)

    if(erros == 4):
        print(" |      \|/   ")
        print(POSTE)
        print(POSTE)

    if(erros == 5):
        print(" |       |    ")
        print(POSTE)

    if(erros == 6):
        print(" |      /     ")

    if (erros == 7):
        print(" |      / \   ")

    print(POSTE)
    print("_|___         ")
    print()

def imprime_mensagem_enforcou(palavra_secreta):
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

def imprime_mensagem_acertou():
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

def marca_chute_correto(palavra_secreta, letras_acertadas, chute, index):
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]

def carrega_palavra_secreta():
    arquivo = open("jogos/palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].strip().upper()

def imprime_mensagem_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()
