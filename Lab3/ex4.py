def creeaza_melodie(note, miscari, start):
    melodie = []
    pozitie = start

    for miscare in miscari:
        if 0 <= pozitie < len(note):
            melodie.append(note[pozitie])
        else:
            melodie.append('X')  # Notele inexistente sau invalide sunt notate cu 'X'

        pozitie += miscare

        while pozitie < 0:
            pozitie += len(note)
        while pozitie >= len(note):
            pozitie -= len(note)

    return melodie

# Exemplu de utilizare:
note_muzicale = ["do", "re", "mi", "fa", "sol"]
miscari = [1, -3, 4, 2]
start = 2

melodie_rezultata = creeaza_melodie(note_muzicale, miscari, start)
print("Melodia formată este:", melodie_rezultata)
