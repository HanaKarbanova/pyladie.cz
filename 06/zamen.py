def zamen(retezec, pozice, znak):
    return retezec[:pozice]+znak+retezec[pozice+1:]

retezec='palec'#input('zadej retezec')
pozice=0#input('na ktere pozici vymenime znak')
znak='v'#input('za dej novy znak')

print("novy retezec je", zamen(retezec, pozice,znak))
