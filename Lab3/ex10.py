def liste_in_tupluri(*listele):
    max_len = max([len(lista) for lista in listele])
    rezultat = []

    for i in range(max_len):
        tuplu = tuple(lista[i] if i < len(lista) else None for lista in listele)
        rezultat.append(tuplu)

    return rezultat

lista1 = [1, 2, 3]
lista2 = [5, 6, 7]
lista3 = ["a", "b", "c"]

rezultat = liste_in_tupluri(lista1, lista2, lista3)
print(rezultat)
