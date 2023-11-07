class Vehicul:
    def __init__(self, marca, model, an):
        self.marca = marca
        self.model = model
        self.an = an

    def calculeaza_consum(self):
        pass

    def calculeaza_capacitate_remorcare(self):
        pass

    def afiseaza_informatii(self):
        print(f"Vehicul: {self.marca} {self.model} din anul {self.an}")

class Masina(Vehicul):
    def __init__(self, marca, model, an, consum_mediu):
        super().__init__(marca, model, an)
        self.consum_mediu = consum_mediu

    def calculeaza_consum(self, distanta):
        return self.consum_mediu * distanta

class Motocicleta(Vehicul):
    def __init__(self, marca, model, an, consum_mediu):
        super().__init__(marca, model, an)
        self.consum_mediu = consum_mediu
    
    def calculeaza_consum(self, distanta):
        return self.consum_mediu * distanta

class Camion(Vehicul):
    def __init__(self, marca, model, an, capacitate_remorcare):
        super().__init__(marca, model, an)
        self.capacitate_remorcare = capacitate_remorcare

    def calculeaza_capacitate_remorcare(self):
        return self.capacitate_remorcare

masina1 = Masina("Ford", "Focus", 2020, 5.7)
motocicleta1 = Motocicleta("Honda", "CBR600RR", 2022, 600)
camion1 = Camion("Volvo", "VNL", 2019, 20000)

masina1.afiseaza_informatii()
print("Consum pentru o călătorie de 200 km:", masina1.calculeaza_consum(200))

motocicleta1.afiseaza_informatii()
print("Consum pentru o călătorie de 200 km:", motocicleta1.calculeaza_consum(200))

camion1.afiseaza_informatii()
print("Capacitate de remorcare:", camion1.calculeaza_capacitate_remorcare())
