def este_prim(numar):
    if numar <= 1:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for i in range(3, int(numar**0.5) + 1, 2):
        if numar % i == 0:
            return False
    return True

def numere_prime_in_lista():
    lista = []
    n = int(input("Introduceți numărul de elemente în listă: "))
    
    for i in range(n):
        numar = int(input(f"Introduceți elementul {i+1}: "))
        lista.append(numar)

    numere_prime = [numar for numar in lista if este_prim(numar)]

    return numere_prime

numere_prime = numere_prime_in_lista()
print("Numerele prime din lista sunt:", numere_prime)
