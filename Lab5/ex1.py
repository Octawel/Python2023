class Forma:
    def __init__(self):
        pass
    
    def calculare_aria(self):
        pass
    
    def calculare_perimetru(self):
        pass

class Cerc(Forma):
    def __init__(self, raza):
        self.raza = raza
    
    def calculare_aria(self):
        return 3.14159 * self.raza ** 2
    
    def calculare_perimetru(self):
        return 2 * 3.14159 * self.raza

class Dreptunghi(Forma):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime
    
    def calculare_aria(self):
        return self.lungime * self.latime
    
    def calculare_perimetru(self):
        return 2 * (self.lungime + self.latime)

class Triunghi(Forma):
    def __init__(self, latura1, latura2, latura3):
        self.latura1 = latura1
        self.latura2 = latura2
        self.latura3 = latura3
    
    def calculare_aria(self):
        s = (self.latura1 + self.latura2 + self.latura3) / 2
        return (s * (s - self.latura1) * (s - self.latura2) * (s - self.latura3)) ** 0.5
    
    def calculare_perimetru(self):
        return self.latura1 + self.latura2 + self.latura3

cerc = Cerc(5)
print(f'Aria cercului: {cerc.calculare_aria()}')
print(f'Perimetrul cercului: {cerc.calculare_perimetru()}')

dreptunghi = Dreptunghi(4, 6)
print(f'Aria dreptunghiului: {dreptunghi.calculare_aria()}')
print(f'Perimetrul dreptunghiului: {dreptunghi.calculare_perimetru()}')

triunghi = Triunghi(3, 4, 5)
print(f'Aria triunghiului: {triunghi.calculare_aria()}')
print(f'Perimetrul triunghiului: {triunghi.calculare_perimetru()}')
