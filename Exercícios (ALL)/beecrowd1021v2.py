n = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = ["1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]
quantidadesN, quantidadesM = [], []

print("NOTAS:")
for nota in notas:
    quantidadesN.append(n//nota)
    n %= nota
[print(f"{qtd:.0f} nota(s) de R$ {nota}.00") for qtd, nota in zip(quantidadesN, notas)]

print("MOEDAS:")
for moeda in moedas:
    if float(moeda) == 0.01:
        quantidadesM.append(n/float(moeda))
    else:
        quantidadesM.append(n//float(moeda))
        n %= float(moeda)
[print(f"{qtd:.0f} moeda(s) de R$ {moeda}") for qtd, moeda in zip(quantidadesM, moedas)]