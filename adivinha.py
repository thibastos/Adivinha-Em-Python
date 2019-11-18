import random

print("\n************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************\n")

numero_secreto = random.randrange(1,100)
print(numero_secreto)

print("Selecione a dificuldade")
print("(1) Fácil    (2) Médio (3) Difícil")
dificuldade = int(input("Escolha: "))
print("\n")

if dificuldade == 1:
    tentativas = 15

if dificuldade == 2:
    tentativas = 10

if dificuldade == 3:
    tentativas = 5

for chutes in range(tentativas):

    print("Tentativa {} de {}".format(chutes, tentativas))
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
