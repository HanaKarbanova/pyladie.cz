for cislo in range(100):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print('BumBac')
    elif cislo % 3 == 0:
        print('Bum')
    elif cislo % 5 == 0:
        print('Bac')
    else:
        print(cislo)
