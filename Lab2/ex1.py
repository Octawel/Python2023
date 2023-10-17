import math

def cmmdc(numere):
    if len(numere) < 2:
        return "Pentru a calcula cmmdc este nevoie de cel putin 2 numere"

    rezultat_cmmdc = numere[0]
    for num in numere[1:]:
        rezultat_cmmdc = math.gcd(rezultat_cmmdc, num)
    return rezultat_cmmdc

try:
    numere_input = input("Introdu numere separate prin spatiu: ")
    numere = list(map(int, numere_input.split()))
    
    gcd = cmmdc(numere)
    print("Cel mai mare divizor comun este:", gcd)

except ValueError:
    print("Input gresit. Introdu numere intregi separate prin spatiu.")
except Exception as e:
    print("Eroare:", str(e))
