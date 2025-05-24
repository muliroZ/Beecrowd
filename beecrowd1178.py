x = float(input())

n = []

i = 100
while i > 0:
    n.append(x)
    x /= 2
    i -= 1

for i in n:
    print(f"N[{n.index(i)}] = {i:.4f}")