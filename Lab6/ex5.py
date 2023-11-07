class Animal:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def emite_sunet(self):
        pass

class Mamifer(Animal):
    def __init__(self, nume, varsta, hrana_preferata):
        super().__init__(nume, varsta)
        self.hrana_preferata = hrana_preferata

    def emite_sunet(self):
        return "Mamiferul scoate sunete specifice."

    def alapteaza(self):
        return "Acest mamifer alăptează puii."

class Pasare(Animal):
    def __init__(self, nume, varsta, tip_zbor):
        super().__init__(nume, varsta)
        self.tip_zbor = tip_zbor

    def emite_sunet(self):
        return "Pasărea cântă minunat."

    def zboara(self):
        return "Această pasăre poate zbura."

class Peste(Animal):
    def __init__(self, nume, varsta, habitat):
        super().__init__(nume, varsta)
        self.habitat = habitat

    def emite_sunet(self):
        return "Peștele nu face sunete."

    def innoata(self):
        return "Acest pește poate înota."


leu = Mamifer("Simba", 5, "carne")
ciocanitoare = Pasare("Woody", 2, "planat")
nemo = Peste("Nemo", 1, "recif de corali")

print(f"{leu.nume} ({leu.varsta} ani) preferă să mănânce {leu.hrana_preferata}. {leu.emite_sunet()}")
print(f"{ciocanitoare.nume} ({ciocanitoare.varsta} ani) poate {ciocanitoare.tip_zbor}. {ciocanitoare.emite_sunet()}")
print(f"{nemo.nume} ({nemo.varsta} ani) trăiește într-un {nemo.habitat}. {nemo.emite_sunet()}")
