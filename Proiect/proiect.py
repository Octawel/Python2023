import copy
import random
import tkinter as tk

class XSiO:
    def __init__(self, dificultate=1):
        self.tabla = [[' ' for _ in range(3)] for _ in range(3)]
        self.jucator_curent = 'X'
        self.castigator = None
        self.dificultate = dificultate
