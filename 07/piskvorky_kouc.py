from random import randint


def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:  # Nikdy nepouzivejte not '-' in pole, je to mene citelne
        return '!'
    else:
        return '-'


def tah(pole, index, symbol):  # Ukazka DRY principu, vytahli jsme spolecny kod do jedne funkce
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if pole[index] != '-':
        raise ValueError('Hrajes na obsazene pole')

    return pole[:index] + symbol + pole[index + 1:]


def tah_hrace(pole):
    """Získá od uživatele pozici, kam chce táhnout, a vrátí pole se zaznamenaným tahem hráče."""
    while True:
        try:
            pozice = int(input('Kam chceš hrát? (0..{})'.format(len(pole) - 1)))
        except ValueError:
            print('Nezadal jsi cislo!')

            #if pozice.isdigit():  # Staci opravdu isdigit?
            #pozice = int(pozice)
        else:
            if pozice < 0 or pozice >= len(pole):
                print('Nemůžeš hrát venku z pole!')
            elif pole[pozice] != '-':
                print('Tam není volno!')
            else:
                return tah(pole, pozice, 'o')



def tah_pocitace(pole):
    """Vrátí herní pole se zaznamenaným tahem počítače."""
    pozice = -1
    while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
        pozice = randint(0, len(pole) - 1)

    return tah(pole, pozice, 'x')


def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace(pole)
        else:
            pole = tah_pocitace(pole)
        print(pole)

        if vyhodnot(pole) == 'o':
            print('Vyhrál hráč.')
        elif vyhodnot(pole) == 'x':
            print('Vyhrál počítač.')
        elif vyhodnot(pole) == '!':
            print('Remíza!')

        if vyhodnot(pole) != '-':
            break

        i += 1
