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
        if terreno[linhas[i]-1][colunas[i]-1] == terreno[linhas[i]-1][colunas[i]] == terreno[linhas[i]-1][colunas[i]+1] == 7:
            if terreno[linhas[i]][colunas[i]-1] == terreno[linhas[i]+1][colunas[i]-1] == terreno[linhas[i]+1][colunas[i]] == 7:
                if terreno[linhas[i]+1][colunas[i]+1] == terreno[linhas[i]][colunas[i]+1] == 7:
                    x = linhas[i] + 1
                    y = colunas[i] + 1
print(x, y)