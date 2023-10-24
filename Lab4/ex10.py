def loop(mapping):
    vizitat = set()
    rezultat = []
    cheie = "start"

    while cheie not in vizitat and cheie in mapping:
        vizitat.add(cheie)
        valoare = mapping[cheie]
        rezultat.append(valoare)
        cheie = valoare

    return rezultat

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
rezultat = loop(mapping)
print(rezultat)
