tah_clovek = input('kámen, nůžky nebo papír?')
tah_pocitac = 'kámen'

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
