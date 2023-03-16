candidatos = {
    1: "Jair Rodrigues",
    2: "Carlos Luz",
    3: "Neves Rocha",
    4: "Nulo",
    5: "Branco"
}

votos = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

num_votos = 0

while True:
    print("As opções são:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votação")
    
    opcao = int(input("Entre com o seu voto: "))
    
    if opcao == 6:
        break
    
    if opcao in votos:
        votos[opcao] += 1
        num_votos += 1
    else:
        print("Opção inválida!")
        continue

num_nulos = votos[4]
num_brancos = votos[5]

porc_nulos = (num_nulos / num_votos) * 100
porc_brancos = (num_brancos / num_votos) * 100

print("Número de votos para cada candidato:")
for chave, valor in votos.items():
    if chave != 4 and chave != 5:
        print(candidatos[chave] + ":", valor)

print("Porcentagem de votos nulos: %.2f%%" % porc_nulos)
print("Porcentagem de votos brancos: %.2f%%" % porc_brancos)

vencedor = max(votos, key=votos.get)
print("Candidato vencedor: " + candidatos[vencedor])