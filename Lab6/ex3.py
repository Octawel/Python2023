import os
import sys

def calculeaza_dimensiune_director(cale_director):
    try:
        dimensiune_totala = 0

        for radacina, directoare, fisiere in os.walk(cale_director):
            for fisier in fisiere:
                cale_fisier = os.path.join(radacina, fisier)
                dimensiune_totala += os.path.getsize(cale_fisier)

        return dimensiune_totala

    except FileNotFoundError:
        return "Directorul nu există."

    except PermissionError:
        return "Nu aveți permisiuni suficiente pentru a accesa fișierele."

    except Exception as e:
        return f"Eroare necunoscută: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python script.py <cale_director>")
        sys.exit(1)

    cale_director = sys.argv[1]

    rezultat = calculeaza_dimensiune_director(cale_director)
    print(f"Dimensiunea totală a fișierelor în '{cale_director}': {rezultat} bytes.")
