peso = int(input())
primos = []

for i in range(peso, 64000):
    primo = 1
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            primo = 0
            break
    
    if primo:
        primos.append(i)
    if len(primos) == 10:
        break

velocidade = sum(primos)
print(f"{velocidade} km/h")
horas = int(60000000/velocidade)
dias = int(horas/24)
print(f"{horas} h / {dias} d")