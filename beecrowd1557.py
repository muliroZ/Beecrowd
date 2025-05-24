while True:
    n = int(input())

    if n == 0: break

    matriz = [[1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != 0:
                matriz[i][0] = matriz[i-1][1]
            if j != 0:
                matriz[i][j] = matriz[i][j-1]*2

    formatacao = len(str(matriz[n-1][n-1]))

    for linha in matriz:
        print(' '.join(f"{str(elemento).rjust(formatacao)}" for elemento in linha))
    print()