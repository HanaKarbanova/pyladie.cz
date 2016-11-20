def tah (pole, cislo_policka, symbol):
    "vrati herní pole s daným symbolem umýstěným na danou pozici"
    return pole[:cislo_policka]+symbol+pole[cislo_policka+1:]
