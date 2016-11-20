def mocniny_2(pocet):
    seznam = []
    for i in range(pocet):
        seznam.append(2**i)
    return seznam

vysledek = mocniny_2(6)
print(vysledek)
