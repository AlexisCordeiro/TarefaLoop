import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    if palpite < 1 or palpite > 100:
        print("Valor inválido. Digite um número entre 1 e 100.")
    elif palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")