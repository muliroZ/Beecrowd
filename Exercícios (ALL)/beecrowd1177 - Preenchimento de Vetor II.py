t = int(input())
numeros = []

for i in range(1000):
    j = 0
    while j < t:
        numeros.append(j)
        j += 1
    print(f"N[{i}] = {numeros[i]}")