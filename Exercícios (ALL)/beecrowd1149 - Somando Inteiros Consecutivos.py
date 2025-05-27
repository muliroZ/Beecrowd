numeros = list(map(int, input().split()))
a = numeros[0]

for x in numeros[1:]:
    if x > 0:
        n = x
        break

soma = sum(a + i for i in range(n))
print(soma)