while True:
    n = int(input())
    if n == 0:
        break

    [print(x, end=" ") for x in range(1, n)]
    print(n)