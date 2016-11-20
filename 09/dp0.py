zvirata = ['pes', "kočka", "králík", "had"]

def kratsu_nez_pet(seznam):
    vystup =[]
    for polozka in seznam:
        if len(polozka) < 5:
            vystup.append(polozka)
    return vystup



print(kratsu_nez_pet(zvirata))
