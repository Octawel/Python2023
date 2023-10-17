def este_palindrom(numar):
    return str(numar) == str(numar)[::-1]

def numere_palindrom(lista):
    palindroame = [numar for numar in lista if este_palindrom(numar)]

    if palindroame:
        cel_mai_mare_palindrom = max(palindroame)
    else:
        cel_mai_mare_palindrom = None

    return len(palindroame), cel_mai_mare_palindrom


numere = [123, 121, 1331, 456, 78987, 98765489]

rezultat = numere_palindrom(numere)
print("Numere palindroame găsite:", rezultat[0])
print("Cel mai mare palindrom găsit:", rezultat[1])
