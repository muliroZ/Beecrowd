# f = fiddle, i = pobre coitado, v = velocidade e, R1 = raio do cast e R2 = raio da ult
# DISTANCIA ENTRE 2 PONTOS MIZERAAAAAAA

while True:
    try:
        Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, input().split())
        distancia = ((Xi - Xf)**2 + (Yi - Yf)**2)**0.5

        if R1 + R2 >= distancia + 1.5 * Vi:
            print("Y")
        else:
            print("N")
    except:
        break