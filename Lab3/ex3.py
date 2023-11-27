def compara_dicționare(dicționar1, dicționar2):
    if type(dicționar1) != type(dicționar2):
        return False

    if len(dicționar1) != len(dicționar2):
        return False

    for cheie, valoare in dicționar1.items():
        if cheie not in dicționar2:
            return False
        if isinstance(valoare, dict):
            if not compara_dicționare(valoare, dicționar2[cheie]):
                return False
        elif isinstance(valoare, list) or isinstance(valoare, set):
            if not valoare == dicționar2[cheie]:
                return False
        else:
            if valoare != dicționar2[cheie]:
                return False

    return True

d1 = {'a': 1, 'b': [1, 2, {'d': 2}, 3], 'c': {'x': 10, 'y': 20}}
d2 = {'a': 1, 'b': [1, 2, {'d': 3}, 3], 'c': {'x': 10, 'y': 20}}

rezultat = compara_dicționare(d1, d2)
print(rezultat) 