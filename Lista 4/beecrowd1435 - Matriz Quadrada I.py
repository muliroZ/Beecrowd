while True:
    # Será uma matriz n x n jae
    n = int(input())

    if n == 0: break

    # Começamos colocando tudo na matriz sendo 1
    matriz = []
    for i in range(n): # Para cada linha
        linha = []
        for j in range(n): # Para cada coluna
            linha.append(1)
        matriz.append(linha) # Adiciona a linha à matriz

    # Variáveis para controlar as bordas da camada atual
    borda = 1 # começa com borda 1 e dps vai aumentando
    cima = 0
    baixo = n - 1
    esquerda = 0
    direita = n - 1

    # Calcula o número de camadas (meio da matriz)
    if n % 2 == 0:
        meio = n/2
    else:
        meio = (n + 1)/2

    # Preenche as camadas da matriz
    while borda <= meio:
        i = esquerda
        while i <= direita:
            matriz[cima][i] = borda
            matriz[baixo][i] = borda
            i += 1

        i = cima + 1
        while i < baixo:
            matriz[i][esquerda] = borda
            matriz[i][direita] = borda
            i += 1

        # Avança para a próxima camada interna
        borda += 1
        cima += 1
        baixo -= 1
        esquerda += 1
        direita -= 1

    # Imprime a matriz naquele modelo
    for i in range(n):
        pular = ''
        for j in range(n):
            pular += f" {matriz[i][j]:3}" # Junta os valores da linha com espaço
        print(pular[1:]) # Remove o primeiro espaço
    print()