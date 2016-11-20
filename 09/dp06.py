zvirata = ["had", "pes", "andulka", "kočka", "králík"]
zvirata.sort()

def rozdvoj(seznam):
    vystupni_seznam = []
    for polozka in seznam:
        dvojice = (polozka[1:],polozka)
        vystupni_seznam.append(dvojice)
    return vystupni_seznam


def sluc(seznam_dvojic):
    vystupni_seznam = []
    for polozka in seznam_dvojic:
        mrsina, zvire = polozka
        vystupni_seznam.append(zvire)
    return vystupni_seznam

print(zvirata)



dvoj_zvirata = rozdvoj(zvirata)
dvoj_zvirata.sort()
zvirata = sluc(dvoj_zvirata)

print(zvirata)
