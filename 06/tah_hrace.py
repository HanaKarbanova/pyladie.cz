from tah import tah

symbol='X'
cislo_policka=int(input("Kam mám umístit znak od 0 do 19?:"))
while cislo_policka <0 or cislo_policka>19:
    print("Hrací pole obsahuje pozice od 0 do 19!")
    cislo_policka = int(input("Zadej znovu pozici:"))
