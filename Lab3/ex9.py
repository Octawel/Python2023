def locuri_nevizibile(matrice):
    n = len(matrice)
    m = len(matrice[0])
    locuri_nevizibile = []

    for i in range(n):
        for j in range(m):
            for k in range(i):
                if matrice[k][j] >= matrice[i][j]:
                    locuri_nevizibile.append((i, j))
                    break

    return locuri_nevizibile

matrice = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
rezultat = locuri_nevizibile(matrice)
print(rezultat) 
