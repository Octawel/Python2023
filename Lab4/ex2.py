class Coada:
    def __init__(self):
        self.elemente = []

    def push(self, element):
        self.elemente.append(element)

    def pop(self):
        if not self.este_goala():
            return self.elemente.pop(0)
        else:
            return None

    def peek(self):
        if not self.este_goala():
            return self.elemente[0]
        else:
            return None

    def este_goala(self):
        return len(self.elemente) == 0

coada = Coada()
coada.push(1)
coada.push(2)
coada.push(3)

print(coada.pop())  # 1
print(coada.peek())  # 2
print(coada.pop())  # 2
print(coada.pop())  # 3
print(coada.pop())  # None
