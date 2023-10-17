def fibbonaci(n):
    fib_list = [] 

    a, b = 0, 1
    fib_list.append(a)
    fib_list.append(b)

    while len(fib_list) < n:
        a, b = b, a + b
        fib_list.append(b)

    return fib_list

n = int(input("Introduceți câte numere Fibonacci doriți: "))
rezultat = fibbonaci(n)
print(rezultat)
