while True:
    n = int(input())
    if n == 0: break

    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(2 ** (i + j))
        matriz.append(linha)
        
    just = len(str(matriz[n-1][n-1]))

    for linha in matriz:
        print(" ".join(f"{num:{just}}" for num in linha))
    print()