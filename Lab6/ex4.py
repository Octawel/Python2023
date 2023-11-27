import os
import sys
from collections import defaultdict

def numara_fisiere_cu_extensii(cale_director):
    try:
        dict_extensii = defaultdict(int)

        for radacina, _, fisiere in os.walk(cale_director):
            for fisier in fisiere:
                _, extensie = os.path.splitext(fisier)
                dict_extensii[extensie] += 1

        # Afișăm rezultatele
        for extensie, numar in dict_extensii.items():
            print(f"{extensie}: {numar} fișiere")

    except FileNotFoundError:
        print("Directorul nu există.")

    except PermissionError:
        print("Nu aveți permisiuni suficiente pentru a accesa fișierele.")

    except Exception as e:
        print(f"Eroare necunoscută: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python script.py <cale_director>")
        sys.exit(1)

    cale_director = sys.argv[1]

    numara_fisiere_cu_extensii(cale_director)
