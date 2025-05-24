caso = 1

while True:
    try:
        n1 = input()
        n2 = input()
        print(f"Caso #{caso}:")
        sub = n2.count(n1)

        if sub == 0:
            print("Nao existe subsequencia")

        else:
            print(f"Qtd.Subsequencias: {sub}")
            pos = n2.rfind(n1)
            print(f"Pos: {pos+1}")
        print()
        caso += 1

    except EOFError:
        break