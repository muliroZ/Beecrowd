while True:
    d, n = input().split()
    if d == '0' and n == '0':
        break

    n = '0' + n
    valor = int(n.replace(d, ''))
    print(valor)