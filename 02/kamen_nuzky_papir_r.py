tah_clovek = input('kámen, nůžky nebo papír?')

from random import randrange
tah_pocitac = randrange(3)

if tah_pocitac == 0:
    tah_pocitac = 'kámen'
elif tah_pocitac == 1:
    tah_pocitac = 'nůžky'
elif tah_pocitac >= 2:
    tah_pocitac = 'papír'


if tah_clovek == 'kámen':
    if tah_pocitac == 'kámen':
        print('remíza')
    elif tah_pocitac == 'nůžky':
        print('Výhra!')
    elif tah_pocitac == 'papír':
        print('Prohra :(')
elif tah_clovek == 'nůžky':
    if tah_pocitac == 'kámen':
        print('Prohra :(')
    elif tah_pocitac == 'nůžky':
        print('Remíza')
    elif tah_pocitac == 'papír':
        print ('Výhra!')
elif tah_clovek == 'papír':
    if tah_pocitac == 'kámen':
        print('Výhra')
    elif tah_pocitac == 'nůžky':
        print('Prohra :(')
    elif tah_pocitac == 'papír':
        print('Remíza')

else:
    print ('Nerozumím!')
