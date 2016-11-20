def delitelnych_3 (vstup):
    od ,do = vstup
    seznam = []
    for i in range (od, do):
        if i % 3 == 0:
            seznam.append(i)
    pocet = len(seznam)
    return (pocet, seznam)

vstup=(67, 102)
pocet_prvku, seznam_prvku = delitelnych_3(vstup)
print('celkem je to', pocet_prvku)
print('konkretne to jsou', seznam_prvku)
