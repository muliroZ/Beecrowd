# 1 = par, 0 = impar

def roubando():
    if r == a and r != 0:
        print("Jogador 2 ganha!")
        return True
    elif r == 1:
        print("Jogador 1 ganha!")
        return True
    elif a == 1:
        print("Jogador 1 ganha!")
        return True
    else:
        return False

p, j1, j2, r, a = map(int, input().split())

soma = j1 + j2

if p == 1:
    if not roubando():
        if soma % 2 == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")

elif p == 0:
    if not roubando():
        if soma % 2 == 0:
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")