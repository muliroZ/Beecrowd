while True:
    n = int(input())

    if n == 0: break

    matriz = []

    for i in range(1, n+1):
        linha = []
        contador = i
        for j in range(n):
            linha.append(abs(contador))
            if contador == 1:
                contador -= 3
            else:
                contador -= 1
        matriz.append(linha)

    for i in range(n):
        pular = ''
        for j in range(n):
            pular += f" {matriz[i][j]:3}"
        print(pular[1:])
    print()