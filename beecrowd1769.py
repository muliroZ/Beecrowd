while True:
    try:
        cpf = [int(num) for num in input().replace('-', ''). replace('.', '')]
        b1, b2 = 0, 0

        for i in range(9):
            b1 += cpf[i]*(i+1)
        b1 %= 11
        for i in range(9):
            b2 += cpf[i]*(9-i)
        b2 %= 11

        if b1 == 10: b1 = 0
        if b2 == 10: b2 = 0
        print("CPF valido") if b1 == cpf[9] and b2 == cpf[10] else print("CPF invalido")

    except EOFError:
        break