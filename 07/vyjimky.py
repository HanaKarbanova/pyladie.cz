velikost_pole = 20

def over_cislo(cislo):
    if 0<= cislo < 20:
        print('OK')
    else:
        raise ValueError('Cislo {n} neni v poli!'.format(n=cislo))

over_cislo(1)
over_cislo(20)
