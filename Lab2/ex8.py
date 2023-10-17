def numara_biti_unu(numar):
    numar_binar = bin(numar)[2:] 
    numar_biti_1 = numar_binar.count('1') 
    
    return numar_binar, numar_biti_1

numar = int(input("Introduceți un număr: "))
bina, biti_unu = numara_biti_unu(numar)

print(f"Reprezentarea binară a numărului {numar} este: {bina}")
print(f"Numărul de biți de 1 în reprezentarea binară este: {biti_unu}")
