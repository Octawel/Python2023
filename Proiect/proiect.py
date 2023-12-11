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

