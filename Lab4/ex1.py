def operatii_cu_seturi(a, b):
    intersectie = set(a) & set(b)
    reuniune = set(a) | set(b)
    diferenta_ab = set(a) - set(b)
    diferenta_ba = set(b) - set(a)

    rezultate = [intersectie, reuniune, diferenta_ab, diferenta_ba]
    return rezultate

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

rezultate = operatii_cu_seturi(a, b)
for rezultat in rezultate:
    print(rezultat)
