class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def afiseaza_informatii(self):
        print(f"Nume: {self.nume}")
        print(f"Prenume: {self.prenume}")
        print(f"Salariu: {self.salariu}")

class Manager(Angajat):
    def __init__(self, nume, prenume, salariu, departament):
        super().__init__(nume, prenume, salariu)
        self.departament = departament

    def afiseaza_informatii(self):
        super().afiseaza_informatii()
        print(f"Departament: {self.departament}")

class Inginer(Angajat):
    def __init__(self, nume, prenume, salariu, proiecte):
        super().__init__(nume, prenume, salariu)
        self.proiecte = proiecte

    def afiseaza_informatii(self):
        super().afiseaza_informatii()
        print(f"Proiecte: {', '.join(self.proiecte)}")

class Vanzator(Angajat):
    def __init__(self, nume, prenume, salariu, regiune):
        super().__init__(nume, prenume, salariu)
        self.regiune = regiune

    def afiseaza_informatii(self):
        super().afiseaza_informatii()
        print(f"Regiune: {self.regiune}")


manager1 = Manager("John", "Doe", 6000, "Vânzări")
inginer1 = Inginer("Alice", "Smith", 7500, ["Proiect A", "Proiect B"])
vanzator1 = Vanzator("Bob", "Johnson", 4000, "Nord")

manager1.afiseaza_informatii()
print()

inginer1.afiseaza_informatii()
print()

vanzator1.afiseaza_informatii()
