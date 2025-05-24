while True:
    try:
        criptografia = {}

        c, n = map(int, input().split())

        cifra1 = input()
        cifra2 = input()
        lCifra1 = cifra1.lower()
        lCifra2 = cifra2.lower()

        for l in range(c):
            criptografia[cifra1[l]] = cifra2[l]
            criptografia[cifra2[l]] = cifra1[l]
            criptografia[lCifra1[l]] = lCifra2[l]
            criptografia[lCifra2[l]] = lCifra1[l]

        for _ in range(n):
            texto = input()
            for char in texto:
                print(criptografia.get(char, char), end="")
            print("")
        print("")
        
    except:
        break