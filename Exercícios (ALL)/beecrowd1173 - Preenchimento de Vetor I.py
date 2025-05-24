n = int(input())
numeros = []
for _ in range(10):
    numeros.append(n)
    n *= 2

for i in numeros:
    print(f"N[{numeros.index(i)}] = {i}")