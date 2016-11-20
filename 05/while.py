#tento program ukazuje cyklus while
text_pro_uzivatele ="zadej cislo, prosim:"
vstup = input(text_pro_uzivatele)

while not vstup.isdigit() :
    print('Tohle není číslo zkus to ještě jednou.')
    vstup = input(text_pro_uzivatele)
print('diky, zadal jsi', vstup, 'cau!')
