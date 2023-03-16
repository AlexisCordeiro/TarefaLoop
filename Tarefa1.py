valor = int(input("Digite um valor inteiro entre 1 e 10: "))

if valor < 1 or valor > 10:
    print("Valor inválido. Digite um valor inteiro entre 1 e 10.")
else:
    print("Tabuada de", valor, ":")
    for i in range(1, 11):
        print(valor, "x", i, "=", valor*i)