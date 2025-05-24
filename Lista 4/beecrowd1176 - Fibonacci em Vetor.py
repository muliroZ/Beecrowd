fibonacci = [0, 1]
primeiro = 0
segundo = 1

for _ in range(60):
    novo_termo = primeiro + segundo
    fibonacci.append(novo_termo)
    primeiro = segundo
    segundo = novo_termo

t = int(input())
for _ in range(t):
    n = int(input())
    print(f"Fib({n}) = {fibonacci[n]}")