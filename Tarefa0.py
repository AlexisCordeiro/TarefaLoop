primeiro = int(input("Digite o primeiro valor: "))
ultimo = int(input("Digite o último valor: "))

if ultimo < primeiro:
    # Contagem decrescente
    for i in range(primeiro, ultimo-1, -1):
        print(i, end=' ')
else:
    # Contagem crescente
    for i in range(primeiro, ultimo+1):
        print(i, end=' ')
    