while True:
    try:
        c, n = map(int, input().split())

        cifra1 = input()
        cifra2 = input()
        lCifra1 = cifra1.lower()
        lCifra2 = cifra2.lower()

        for _ in range(n):
            frase = input()
            nova_frase = ""

            for char in frase:
                if char in cifra1:
                    nova_frase += cifra2[cifra1.index(char)]
                elif char in cifra2:
                    nova_frase += cifra1[cifra2.index(char)]
                elif char in lCifra1:
                    nova_frase += lCifra2[lCifra1.index(char)]
                elif char in lCifra2:
                    nova_frase += lCifra1[lCifra2.index(char)]
                else:
                    nova_frase += char
            
            print(nova_frase)
        print()
        
    except EOFError:
        break