teplota_vody=float(input('Kolik má voda stupňů?'))

if teplota_vody >100:
    print('Voda se vaří')
elif teplota_vody >=80:
    print('Už se skoro vaří')
elif teplota_vody >= 45:
    print ('Voda na zalití zaleného čaje')
elif teplota_vody >= 38:
    print('Už začíná být vařící')
elif teplota_vody >= 34:
    print('Píjemná teplota na koupání')
elif teplota_vody >= 20:
    print('Vlažná voda')
elif teplota_vody >=-5:
    print("Ta je studená")
else:
    print('To už je led')
