#Zde se pocita obsah ctverce
strana= float(input('velikost strany v centimetrech:'))
strana_je_spravna=strana>=0

if strana_je_spravna:
    print("Obvod čtverce se stranou", strana, "cm je", 4*strana, "cm" )
# obvod ctverce
    print("Obsah čtverce se stranou", strana, "cm je", strana**2, "cm2")

    polomer=strana
    pi=3.1415926
    #obvod kruhu
    print("Obvod kruhu s polomere", polomer, "cm je", 2*pi*polomer, "cm" )
    #obsah kruhu
    print("Obsah kruhu s polomerem", polomer, "cm je", pi*polomer**2, "cm2")

else:
    print("Záporné číslo")

print("Děkujeme za použití kalkulačky")
