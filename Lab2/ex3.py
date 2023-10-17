def numar_aparitii(sir1, sir2):
    numar_aparitii = 0
    index = sir2.find(sir1)

    while index != -1:
        numar_aparitii += 1
        index = sir2.find(sir1, index + 1)

    return numar_aparitii

sir1 = input("Introduceți primul șir: ")
sir2 = input("Introduceți al doilea șir: ")

rezultat = numar_aparitii(sir1, sir2)

print(f"Șirul '{sir1}' apare de {rezultat} ori în șirul '{sir2}'.")
