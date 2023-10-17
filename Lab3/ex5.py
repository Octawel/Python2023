def diagonala_principala_la_0(matrice):
    if not matrice:
        return matrice

    num_rows, num_cols = len(matrice), len(matrice[0])

    for i in range(min(num_rows, num_cols)):
        matrice[i][i] = 0

    return matrice

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrice_modificata = diagonala_principala_la_0(matrice)
for linie in matrice_modificata:
    print(linie)
