def grupare_după_rimă(cuvinte):
    grupuri_rimă = {}

    for cuvant in cuvinte:
        rima = cuvant[-2:]
        if rima not in grupuri_rimă:
            grupuri_rimă[rima] = [cuvant]
        else:
            grupuri_rimă[rima].append(cuvant)

    rezultat = list(grupuri_rimă.values())
    return rezultat

cuvinte = ['ana', 'banana', 'carte', 'arme', 'parte']
rezultat = grupare_după_rimă(cuvinte)
print(rezultat)
