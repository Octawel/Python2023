def numara_argumente_valabile(*args, **kwargs):
    contor = 0
    
    for arg in args:
        if arg in kwargs.values():
            contor += 1
    return contor

rezultat = numara_argumente_valabile(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(rezultat)
