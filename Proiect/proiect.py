import copy
import random
import tkinter as tk

class XSiO:
    def __init__(self, dificultate=1):
        self.tabla = [[' ' for _ in range(3)] for _ in range(3)]
        self.jucator_curent = 'X'
        self.castigator = None
        self.dificultate = dificultate

    def face_mutare(self, linie, coloana):
        if self.tabla[linie][coloana] == ' ' and not self.este_sfidat():
            self.tabla[linie][coloana] = self.jucator_curent
            self.verifica_castigator()
            self.schimba_jucator()
    
    def schimba_jucator(self):
        self.jucator_curent = 'O' if self.jucator_curent == 'X' else 'X'

    def este_sfidat(self):
        return self.castigator is not None or all(all(celula != ' ' for celula in rand) for rand in self.tabla)

    def verifica_castigator(self):
        for i in range(3):
            if self.tabla[i][0] == self.tabla[i][1] == self.tabla[i][2] != ' ':
                self.castigator = self.tabla[i][0]
                return
            if self.tabla[0][i] == self.tabla[1][i] == self.tabla[2][i] != ' ':
                self.castigator = self.tabla[0][i]
                return
        if self.tabla[0][0] == self.tabla[1][1] == self.tabla[2][2] != ' ':
            self.castigator = self.tabla[0][0]
        elif self.tabla[0][2] == self.tabla[1][1] == self.tabla[2][0] != ' ':
            self.castigator = self.tabla[0][2]

    def obtine_celule_libere(self):
        return [(i, j) for i in range(3) for j in range(3) if self.tabla[i][j] == ' ']

    def ia_mutare_optima(self):
        if self.dificultate == 1:
            linie, coloana = random.choice(self.obtine_celule_libere())
        elif self.dificultate == 2:
            if random.random() < 0.5:
                linie, coloana = random.choice(self.obtine_celule_libere())
            else:
                linie, coloana = self.obtine_mutare_optima()
        else:
            linie, coloana = self.obtine_mutare_optima()

        self.face_mutare(linie, coloana)

    def obtine_mutare_optima(self):
        _, (linie, coloana) = self.minmax(self.tabla, True)
        return linie, coloana

    def minmax(self, tabla, maximizingPlayer):
        celule_libere = self.obtine_celule_libere()

        if self.verifica_mutare_castigatoare(tabla, 'X'):
            return -10, None
        elif self.verifica_mutare_castigatoare(tabla, 'O'):
            return 10, None
        elif not celule_libere:
            return 0, None

        if maximizingPlayer:
            maxEval = float("-inf")
            cea_mai_buna_mutare = None
            for celula in celule_libere:
                tabla[celula[0]][celula[1]] = 'O'
                evaluare, _ = self.minmax(tabla, False)
                tabla[celula[0]][celula[1]] = ' '
                if evaluare > maxEval:
                    maxEval = evaluare
                    cea_mai_buna_mutare = celula
            return maxEval, cea_mai_buna_mutare
        else:
            minEval = float("inf")
            cea_mai_buna_mutare = None
            for celula in celule_libere:
                tabla[celula[0]][celula[1]] = 'X'
                evaluare, _ = self.minmax(tabla, True)
                tabla[celula[0]][celula[1]] = ' '
                if evaluare < minEval:
                    minEval = evaluare
                    cea_mai_buna_mutare = celula
            return minEval, cea_mai_buna_mutare
        
    def verifica_mutare_castigatoare(self, tabla, jucator):
        for i in range(3):
            if tabla[i][0] == tabla[i][1] == tabla[i][2] == jucator or \
               tabla[0][i] == tabla[1][i] == tabla[2][i] == jucator:
                return True
        if tabla[0][0] == tabla[1][1] == tabla[2][2] == jucator or \
           tabla[0][2] == tabla[1][1] == tabla[2][0] == jucator:
            return True
        return False
    
class InterfataXSiO:
    def __init__(self, root, joc):
        self.root = root
        self.root.title("X și O")
        self.joc = joc

        self.butoane = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.butoane[i][j] = tk.Button(root, text='', font=('normal', 20), width=5, height=2,
                                              command=lambda linie=i, coloana=j: self.on_click(linie, coloana))
                self.butoane[i][j].grid(row=i, column=j)

        self.variabila_dificultate = tk.StringVar()
        self.variabila_dificultate.set("1")
        self.meniu_dificultate = tk.OptionMenu(root, self.variabila_dificultate, "1", "2", "3")
        self.meniu_dificultate.grid(row=3, column=0, pady=10)

        self.butoane_resetare = tk.Button(root, text='Resetează', font=('normal', 14), width=10, command=self.reseteaza_joc)
        self.butoane_resetare.grid(row=3, column=1, pady=10)

        self.eticheta_mesaj = tk.Label(root, text='', font=('normal', 16))
        self.eticheta_mesaj.grid(row=4, column=0, columnspan=3)

        self.reseteaza_joc()

    def on_click(self, linie, coloana):
        if self.joc.tabla[linie][coloana] == ' ' and not self.joc.este_sfidat():
            self.joc.face_mutare(linie, coloana)
            self.actualizeaza_tabla()
            if not self.joc.este_sfidat() and self.joc.jucator_curent == 'O':
                self.joc.ia_mutare_optima()
                self.actualizeaza_tabla()

    def actualizeaza_tabla(self):
        for i in range(3):
            for j in range(3):
                self.butoane[i][j].config(text=self.joc.tabla[i][j])

        if self.joc.este_sfidat():
            if self.joc.castigator:
                self.eticheta_mesaj.config(text=f"Câștigător: {self.joc.castigator}")
            else:
                self.eticheta_mesaj.config(text="E remiză!")
        else:
            self.eticheta_mesaj.config(text=f"Jucător curent: {self.joc.jucator_curent}")

    def reseteaza_joc(self):
        dificultate = int(self.variabila_dificultate.get())
        self.joc = XSiO(dificultate)
        self.actualizeaza_tabla()


if __name__ == "__main__":
    root = tk.Tk()
    joc = XSiO()
    app = InterfataXSiO(root, joc)
    root.mainloop()

