def operatii_cu_liste(a, b):
    intersectie = list(set(a) & set(b))
    reuniune = list(set(a) | set(b))  
    diferenta_a_b = list(set(a) - set(b))  
    diferenta_b_a = list(set(b) - set(a))  
    
    return intersectie, reuniune, diferenta_a_b, diferenta_b_a


lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]

inter, un, a_minus_b, b_minus_a = operatii_cu_liste(lista_a, lista_b)

print("Intersecția a și b:", inter)
print("Reuniunea a și b:", un)
print("Diferența a - b:", a_minus_b)
print("Diferența b - a:", b_minus_a)
