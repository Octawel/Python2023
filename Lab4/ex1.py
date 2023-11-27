class Stiva:
    def __init__(self):
        self.elemente = []

    def push(self, element):
        self.elemente.append(element)

    def pop(self):
        if not self.este_goala():
            return self.elemente.pop()
        else:
            return None

    def peek(self):
        if not self.este_goala():
            return self.elemente[-1]
        else:
            return None

    def este_goala(self):
        return len(self.elemente) == 0

stiva = Stiva()
stiva.push(1)
stiva.push(2)
stiva.push(3)

print(stiva.pop())  # 3
print(stiva.peek())  # 2
print(stiva.pop())  # 2
print(stiva.pop())  # 1
print(stiva.pop())  # None
