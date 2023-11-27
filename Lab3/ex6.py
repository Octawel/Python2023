def numara_elemente_unice_si_duplicate(lista):
    set_elemente_unice = set()
    set_elemente_duplicate = set()
    
    for element in lista:
        if element in set_elemente_unice:
            set_elemente_duplicate.add(element)
        else:
            set_elemente_unice.add(element)
    
    numar_elemente_unice = len(set_elemente_unice)
    numar_elemente_duplicate = len(set_elemente_duplicate)
    
    return (numar_elemente_unice, numar_elemente_duplicate)

lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
rezultat = numara_elemente_unice_si_duplicate(lista)
print(rezultat)
