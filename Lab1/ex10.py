def numara_cuvinte(propozitie):
    cuvinte = propozitie.split()

    for cuvant in cuvinte:
        if "  " in cuvant:
            raise ValueError("Propoziția conține mai mult de un spațiu între cuvinte.")

    return len(cuvinte)

propozitie = input("Introduceți o propoziție: ")

try:
    numar_cuvinte = numara_cuvinte(propozitie)
    print(f"Propoziția conține {numar_cuvinte} cuvinte.")
except ValueError as e:
    print(e)
