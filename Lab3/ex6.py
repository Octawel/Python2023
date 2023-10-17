def elemente_de_x_ori_in_liste(x, *liste):
    frecventa = {} #dictionar

    for lista in liste:
        for element in lista:
            if element in frecventa:
                frecventa[element] += 1
            else:
                frecventa[element] = 1

    elemente_de_x_ori = [element for element, frec in frecventa.items() if frec == x]

    return elemente_de_x_ori

lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
lista3 = [4, 5, 6]
lista4 = [4, 1, "test"]
x = 2

rezultat = elemente_de_x_ori_in_liste(x, lista1, lista2, lista3, lista4)
print("Elementele care apar de", x, "ori în liste sunt:", rezultat)
