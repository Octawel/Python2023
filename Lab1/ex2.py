def numara_vocale(sir):
    vocale = "aeiouAEIOU"
    numar_vocale = 0

    for caracter in sir:
        if caracter in vocale:
            numar_vocale += 1

    return numar_vocale

text = input("Introduceți un șir de caractere: ")
rezultat = numara_vocale(text)

print(f"În șirul '{text}' sunt {rezultat} vocale.")
