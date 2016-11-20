from random import randint

cislo=randint(1,20)

print("Myslím si číslo od 1 do 20")
#print("psst, je to ",cislo)

pocet_pokusu = 1
vyhra = False

while pocet_pokusu <=6 and not vyhra:

    tip = int(input("Zadej tvuj tip:"))

    if tip==cislo:
        print("Hura, spravne.")
        #break
        vyhra = True
    elif tip < cislo:
        print("Spatne, myslim si vetsi cislo")
    elif tip > cislo:
        print("Spatne, myslim si mensi cislo")
    pocet_pokusu += 1
