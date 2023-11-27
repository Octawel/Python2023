def este_palindrom(numar):
    ok = 0
    numar_str = str(numar)
    numar_invers = numar_str[::-1]

    return numar_str == numar_invers

print(este_palindrom(123))
