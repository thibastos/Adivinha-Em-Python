import random

print("\n************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************\n")

numero_secreto = random.randrange(1,100)
print(numero_secreto)

print("Selecione a dificuldade")
print("(1) Fácil    (2) Médio (3) Difícil")
dificuldade = int(input("Escolha: "))


for tentativas in range(1, 6):

    chute = int(input("Digite um número: "))

    if chute <= 0 :
        print("Digite um número positivo!")
        continue;

    if chute == numero_secreto:
        print("Você acertou!")
        break;

    else:
        if chute > numero_secreto:
            print("Você chutou um número maior!\n")
        else:
            print("Você chutou um número menor!\n")

print("Fim de jogo!")
