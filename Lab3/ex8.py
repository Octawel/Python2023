def caractere_divizibile_x(x=1, siruri=[], flag=True):
    rezultat = []

    for sir in siruri:
        lista_caractere = []
        for caracter in sir:
            cod_ascii = ord(caracter)
            if (cod_ascii % x == 0) if flag else (cod_ascii % x != 0):
                lista_caractere.append(caracter)
        rezultat.append(lista_caractere)

    return rezultat

x = 2
siruri = ["test", "hello", "lab002"]
flag = False

rezultat = caractere_divizibile_x(x, siruri, flag)
print(rezultat)
