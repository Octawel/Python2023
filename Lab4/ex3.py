class Matrice:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrice = [[0] * m for _ in range(n)]

    def get_element(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrice[i][j]
        else:
            return None

    def set_element(self, i, j, valoare):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrice[i][j] = valoare

    def transpose(self):
        transpusa = Matrice(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transpusa.set_element(j, i, self.get_element(i, j))
        return transpusa

    def inmultire_matrice(self, alta_matrice):
        if self.m != alta_matrice.n:
            return None
        if self.n != alta_matrice.m:
            return None

        rezultat = Matrice(self.n, alta_matrice.m)
        for i in range(self.n):
            for j in range(alta_matrice.m):
                valoare = 0
                for k in range(self.m):
                    valoare += self.get_element(i, k) * alta_matrice.get_element(k, j)
                rezultat.set_element(i, j, valoare)
        return rezultat

    def aplica_functie(self, functie):
        for i in range(self.n):
            for j in range(self.m):
                valoare = self.get_element(i, j)
                self.set_element(i, j, functie(valoare))

    def itereaza(self, functie):
        for i in range(self.n):
            for j in range(self.m):
                valoare = self.get_element(i, j)
                functie(i, j, valoare)

matrice = Matrice(2, 3)
matrice.set_element(0, 0, 1)
matrice.set_element(0, 1, 2)
matrice.set_element(0, 2, 3)
matrice.set_element(1, 0, 4)
matrice.set_element(1, 1, 5)
matrice.set_element(1, 2, 6)

# Afișare
for i in range(2):
    for j in range(3):
        print(matrice.get_element(i, j), end=" ")
    print()

# Transpusa
transpusa = matrice.transpose()
print("Transpusa:")
for i in range(3):
    for j in range(2):
        print(transpusa.get_element(i, j), end=" ")
    print()

# Înmulțire
matrice2 = Matrice(3, 2)
matrice2.set_element(0, 0, 1)
matrice2.set_element(0, 1, 2)
matrice2.set_element(1, 0, 3)
matrice2.set_element(1, 1, 4)
matrice2.set_element(2, 0, 5)
matrice2.set_element(2, 1, 6)

rezultat_inmultire = matrice.inmultire_matrice(matrice2)
print("Înmulțirea matricelor:")
for i in range(2):
    for j in range(2):
        print(rezultat_inmultire.get_element(i, j), end=" ")
    print()

# Aplicare
matrice.aplica_functie(lambda x: x * 2)
print("Matricea după aplicarea funcției:")
for i in range(2):
    for j in range(3):
        print(matrice.get_element(i, j), end=" ")
    print()

# Iterare
def afiseaza_element(i, j, valoare):
    print(f"Elementul de la ({i}, {j}) are valoarea {valoare}")

matrice.itereaza(afiseaza_element)
