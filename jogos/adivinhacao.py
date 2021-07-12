import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto_init = 1
    numero_secreto_fim = 100
    numero_secreto = random.randrange(numero_secreto_init, numero_secreto_fim + 1)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute_str = input(f"Digite um número entre {numero_secreto_init} e {numero_secreto_fim}: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(f"Você deve digitar um número entre {numero_secreto_init} e {numero_secreto_fim}!")
            continue

        print("Você digitou:", chute)

        if (numero_secreto == chute):
            print(f"Você acertou e fez {pontos}!")
            break
        else:
            if (chute > numero_secreto):
                print("Você errou! Seu chute foi maior que número secreto.")
            else:
                print("Você errou! Seu chute foi menor que número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo.")

if (__name__ == "__main__"):
    jogar()
