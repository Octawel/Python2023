def litera_cea_mai_comuna(sir):
    sir = sir.lower() 
    frecventa = {}

    for caracter in sir:
        if 'a' <= caracter <= 'z':
            if caracter in frecventa:
                frecventa[caracter] += 1
            else:
                frecventa[caracter] = 1

    if not frecventa:
        return None, 0  
    litera_maxima = max(frecventa, key=frecventa.get)
    aparitii = frecventa[litera_maxima]

    return litera_maxima, aparitii

text = input("Introduceți un șir de caractere: ")
litera, aparitii = litera_cea_mai_comuna(text)

if litera is not None:
    print(f"Litera cea mai comună este '{litera}' și apare de {aparitii} ori.")
else:
    print("Nu au fost găsite litere de la 'a' la 'z' în șir.")
