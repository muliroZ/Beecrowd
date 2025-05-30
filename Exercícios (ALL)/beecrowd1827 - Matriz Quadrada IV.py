while True:
    try:
        n = int(input())
        local_meio = int(n/3)
        meio_supremo = n - local_meio

        matriz = [[0] * n for _ in range(n)]

        for i in range(n):
            matriz[i][i] = 2

        j = 0
        for i in range(n-1, -1, -1):
            matriz[j][i] = 3
            j += 1

        for i in range(local_meio, meio_supremo):
            for j in range(local_meio, meio_supremo):
                matriz[i][j] = 1

        matriz[int(n/2)][int(n/2)] = 4

        for i in range(n):
            pular = ''
            for j in range(n):
                pular += f"{matriz[i][j]}"
            print(pular[:])
        print()

    except EOFError:
        break