while True:
    dama_x, dama_y, casa_x, casa_y = (int(x) for x in input().split())

    if dama_x + dama_y + casa_x + casa_y == 0:
        break

    if dama_x == casa_x and dama_y == casa_y:
        print(0)
    elif dama_x == casa_x or dama_y == casa_y:
        print(1)
    elif abs(dama_x - casa_x) == abs(dama_y - casa_y):
        print(1)
    else: 
        print(2)