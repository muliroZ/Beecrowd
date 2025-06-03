while True:
    n = int(input())
    if n == 0: break

    matriz = [[1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matriz[i][j] = min(i, j, n-i-1, n-j-1) + 1

    for i in range(n):
        matriz_txt = ""
        for j in range(n):
            matriz_txt += f" {matriz[i][j]:3}"
        print(matriz_txt[1:])
    print()