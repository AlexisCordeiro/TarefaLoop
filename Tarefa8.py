capital_inicial = float(input("Digite o valor inicial que deseja investir na poupança: "))
taxa_juros = 0.005   # taxa de juros de 0,5% ao mês
num_meses = 12       # investimento de 12 meses

for mes in range(1, num_meses+1):
    montante = capital_inicial * (1 + taxa_juros)**mes
    print(f"Montante após {mes} meses: R${montante:.2f}")