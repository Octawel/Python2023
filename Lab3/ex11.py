def sorteaza_tupluri(lista_tupluri):
    return sorted(lista_tupluri, key=lambda tuplu: tuplu[1][2])

tuplu1 = ('abc', 'bcd')
tuplu2 = ('abc', 'zza')
lista_tupluri = [tuplu1, tuplu2]

rezultat = sorteaza_tupluri(lista_tupluri)
print(rezultat)
