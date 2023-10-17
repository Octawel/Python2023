def inlocuieste_sub_diagonala_principala_cu_zero(matrice):
    numar_rinduri = len(matrice)
    numar_coloane = len(matrice[0]) if numar_rinduri > 0 else 0

    for rind in range(numar_rinduri):
        for coloana in range(numar_coloane):
            if coloana < rind:
                matrice[rind][coloana] = 0

    return matrice

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rezultat = inlocuieste_sub_diagonala_principala_cu_zero(matrice)
for rind in rezultat:
    print(rind)
