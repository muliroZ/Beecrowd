x, y = [int(i) for i in input().split()]
contador = 0

for i in range(1, y+1, x):
    for j in range(1, x+1):
        if j % x == 0:
            print(j+contador)
            break
        print(j+contador, end=" ")
    contador += x