# Usando list comprehension

n = int(input())
print(n)

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

for nota in notas:
    quantidades.append(n//nota)
    n %= nota

[print(f"{qtd} nota(s) de R$ {nota},00") for qtd, nota in zip(quantidades, notas)]