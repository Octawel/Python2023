class ElementBiblioteca:
    def __init__(self, titlu, autor, an_publicare):
        self.titlu = titlu
        self.autor = autor
        self.an_publicare = an_publicare
        self.disponibil = True

    def verifica_disponibilitate(self):
        return self.disponibil

    def imprumuta(self):
        if self.disponibil:
            self.disponibil = False
            return f"{self.titlu} a fost imprumutata."
        else:
            return f"{self.titlu} nu este disponibila pentru imprumut."

    def returneaza(self):
        if not self.disponibil:
            self.disponibil = True
            return f"{self.titlu} a fost returnata cu succes."
        else:
            return f"{self.titlu} nu poate fi returnata, deoarece nu a fost imprumutata."

    def afiseaza_informatii(self):
        return f"Titlu: {self.titlu}\nAutor: {self.autor}\nAn publicare: {self.an_publicare}\nDisponibila: {self.disponibil}"

class Carte(ElementBiblioteca):
    def __init__(self, titlu, autor, an_publicare, gen):
        super().__init__(titlu, autor, an_publicare)
        self.gen = gen

    def afiseaza_informatii(self):
        return super().afiseaza_informatii() + f"\nGen: {self.gen}"

class DVD(ElementBiblioteca):
    def __init__(self, titlu, regizor, an_publicare, durata):
        super().__init__(titlu, regizor, an_publicare)
        self.durata = durata

    def afiseaza_informatii(self):
        return super().afiseaza_informatii() + f"\nDurata: {self.durata} minute"

class Revista(ElementBiblioteca):
    def __init__(self, titlu, editor, an_publicare, numar):
        super().__init__(titlu, editor, an_publicare)
        self.numar = numar

    def afiseaza_informatii(self):
        return super().afiseaza_informatii() + f"\nNumar: {self.numar}"


carte = Carte("Povestea unui leu", "Alice", 2005, "Fictiune")
dvd = DVD("Filmul meu preferat", "John", 2020, 120)
revista = Revista("Natura vie", "Maria", 2022, 15)

print(carte.afiseaza_informatii())
print(carte.imprumuta())
print(carte.returneaza())
print(carte.afiseaza_informatii())

print(dvd.afiseaza_informatii())
print(dvd.imprumuta())
print(dvd.afiseaza_informatii())

print(revista.afiseaza_informatii())
print(revista.imprumuta())
