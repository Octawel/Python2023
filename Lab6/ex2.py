import os

def redenumeste_fisiere(director):
    try:
        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul {director} nu există.")

        fisiere = os.listdir(director)

        for i, fisier in enumerate(fisiere, start=1):
            vechi_path = os.path.join(director, fisier)
            nume, extensie = os.path.splitext(fisier)
            nou_path = os.path.join(director, f"file{i}{extensie}")

            os.rename(vechi_path, nou_path)

        print("Fișierele au fost redenumite cu succes.")
    
    except FileNotFoundError as e:
        print(f"Eroare: {e}")
    
    except Exception as e:
        print(f"A intervenit o eroare neașteptată: {e}")

director_specificat = input("Introduceți calea către director: ")
redenumeste_fisiere(director_specificat)
