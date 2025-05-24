def cont_impar():
    index = 0
    for num in impar:
        print(f"impar[{index}] = {num}")
        index += 1

def cont_par():
    index = 0
    for num in par:
        print(f"par[{index}] = {num}")
        index += 1

par, impar = [], []

for _ in range(15):
    n = int(input())

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    if len(impar) == 5:
        cont_impar()
        impar = []
    
    if len(par) == 5:
        cont_par()
        par = []

if len(impar) > 0:
    cont_impar()

if len(par) > 0:
    cont_par()