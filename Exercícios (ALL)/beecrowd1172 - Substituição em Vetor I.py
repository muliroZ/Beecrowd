numeros = []
for _ in range(10):
    numeros.append(int(input()))

for j in numeros:
    if j <= 0:
        print(f"X[{numeros.index(j)}] = 1")
    else:
        print(f"X[{numeros.index(j)}] = {j}")