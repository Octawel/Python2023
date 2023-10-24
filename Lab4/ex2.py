def numar_aparitii_caractere(text):
    dictionar_aparitii = {} 

    for caracter in text:
        if caracter in dictionar_aparitii:
            dictionar_aparitii[caracter] += 1
        else:
            dictionar_aparitii[caracter] = 1

    return dictionar_aparitii

text = "Ana has apples."
rezultat = numar_aparitii_caractere(text)
print(rezultat)
