def compune_melodie(note, miscari, start):
    melodie = []
    pozitie = start

    for miscare in miscari:
        while miscare < 0:
            miscare += len(note)
        while miscare >= len(note):
            miscare -= len(note)

        melodie.append(note[pozitie])
        pozitie = (pozitie + miscare) % len(note)

    return melodie

note = ["do", "re", "mi", "fa", "sol"]
miscari = [1, -3, 4, 2]
start = 2

rezultat = compune_melodie(note, miscari, start)
print(rezultat)
