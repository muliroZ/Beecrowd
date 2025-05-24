n, m = [int(x) for x in input().split()]
terreno = []
linhas, colunas = [], []

for i in range(n):
    terreno.append([int(x) for x in input().split()])
    if i > 0 and i < n - 1 and 42 in terreno[i]:
        locais = [local for local, x in enumerate(terreno[i]) if x == 42]
        linhas.extend([i] * len(locais))
        colunas.extend(locais)

x, y = 0, 0
for i in range(len(linhas)):
    if linhas[i] > 0 and linhas[i] < n - 1 and colunas[i] > 0 and colunas[i] < m - 1:
        soma = 0
        for i2 in range(linhas[i] - 1, linhas[i] + 2):
            for j2 in range(colunas[i] - 1, colunas[i] + 2):
                soma += terreno[i2][j2]
        if soma == 98:
            x = linhas[i] + 1
            y = colunas[i] + 1
            break
print(x, y)