def operatii_cu_seturi(*seturi):
    rezultat = {}

    for i in range(len(seturi)):
        for j in range(i + 1, len(seturi)):
            set1 = seturi[i]
            set2 = seturi[j]

            cheie_reuniune = f"{set1} | {set2}"
            rezultat[cheie_reuniune] = set1 | set2

            cheie_intersectie = f"{set1} & {set2}"
            rezultat[cheie_intersectie] = set1 & set2

            cheie_diferenta_ab = f"{set1} - {set2}"
            rezultat[cheie_diferenta_ab] = set1 - set2

            cheie_diferenta_ba = f"{set2} - {set1}"
            rezultat[cheie_diferenta_ba] = set2 - set1

    return rezultat

set1 = {1, 2}
set2 = {2, 3}

rezultat = operatii_cu_seturi(set1, set2)
for cheie, valoare in rezultat.items():
    print(f"{cheie}: {valoare}")
