def nacti_cislo():
    odpoved = input('Zadej cislo:')
    try:
        cislo = int(odpoved)
    except ValueError:
        print('To neni cislo')

nacti_cislo()
