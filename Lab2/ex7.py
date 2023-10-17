def extrage_primul_numar(text):
    numar = ""
    for caracter in text:
        if caracter.isdigit() or caracter == '.':
            numar += caracter
        elif numar:
            break
    try:
        return float(numar)
    except ValueError:
        return None

text = input("Introduceți un text: ")
primul_numar = extrage_primul_numar(text)

if primul_numar is not None:
    print(f"Primul număr din text este: {primul_numar}")
else:
    print("Nu s-a găsit niciun număr în text.")
