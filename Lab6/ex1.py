import os
import sys

def citeste_fisier(director, fisier):
    try:
        cale_fisier = os.path.join(director, fisier)
        with open(cale_fisier, 'r') as file:
            continut = file.read()
            print(f"\nContinutul fisierului {fisier} ({os.path.splitext(fisier)[1]}):")
            print(continut)
    except Exception as e:
        print(f"Eroare la citirea fisierului {fisier}: {str(e)}")

def cautare_fisiere(director, extensie):
    try:
        fisiere_gasite = [f for f in os.listdir(director) if f.endswith(extensie)]
        if not fisiere_gasite:
            print(f"Niciun fisier cu extensia '{extensie}' gasit in directorul {director}")
            return

        print(f"Fisiere gasite in directorul {director} cu extensia '{extensie}':")
        for fisier in fisiere_gasite:
            citeste_fisier(director, fisier)
    except FileNotFoundError:
        print(f"Directorul {director} nu exista.")
    except PermissionError:
        print(f"Nu aveti permisiunea de a accesa fisierele din directorul {director}.")
    except Exception as e:
        print(f"Eroare la cautarea si citirea fisierelor: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <director> <extensie>")
    else:
        director = sys.argv[1]
        extensie = sys.argv[2]
        cautare_fisiere(director, extensie)
