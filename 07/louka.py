Barva_travy = "zelena"
Pocet_kotatek = 28

def popis_stav():
    return 'Trava je {barva}. Prohrani se po ni {pocet} kotatek'. format(
    barva = Barva_travy, pocet = Pocet_kotatek)
