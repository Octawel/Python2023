class Cont:
    def __init__(self, nume_titular, sold_initial):
        self.nume_titular = nume_titular
        self.sold = sold_initial

    def depune(self, suma):
        if suma > 0:
            self.sold += suma
            print(f'Depunere de {suma} RON în contul lui {self.nume_titular}.')
        else:
            print('Suma trebuie să fie mai mare decât 0.')

    def retrage(self, suma):
        if 0 < suma <= self.sold:
            self.sold -= suma
            print(f'Retragere de {suma} RON din contul lui {self.nume_titular}.')
        elif suma <= 0:
            print('Suma trebuie să fie mai mare decât 0.')
        else:
            print('Fonduri insuficiente.')

    def calculeaza_dobanda(self):
        pass

    def afiseaza_sold(self):
        print(f'Soldul curent al lui {self.nume_titular} este de {self.sold} RON.')

class ContEconomii(Cont):
    def __init__(self, nume_titular, sold_initial, rata_dobanda):
        super().__init__(nume_titular, sold_initial)
        self.rata_dobanda = rata_dobanda

    def calculeaza_dobanda(self):
        dobanda = self.sold * self.rata_dobanda
        self.sold += dobanda
        print(f'Dobânda de {dobanda} RON a fost adăugată la contul lui {self.nume_titular}.')

class ContCurent(Cont):
    def __init__(self, nume_titular, sold_initial, comision_retragere):
        super().__init__(nume_titular, sold_initial)
        self.comision_retragere = comision_retragere

    def retrage(self, suma):
        suma_totala = suma + self.comision_retragere
        super().retrage(suma_totala)


cont1 = ContEconomii("Alice", 1000, 0.05)
cont2 = ContCurent("Bob", 500, 2)

cont1.afiseaza_sold()
cont1.depune(200)
cont1.calculeaza_dobanda()
cont1.afiseaza_sold()

cont2.afiseaza_sold()
cont2.retrage(100)
cont2.afiseaza_sold()
