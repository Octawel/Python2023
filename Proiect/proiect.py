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
