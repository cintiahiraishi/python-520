
class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    #(1,3)+(3,5) = (4,0)
    def add(self, vetor):
        self.x += vetor.x
        self.y += vetor.y

    def sub(self, vetor):
        self.x -= vetor.x
        self.y -= vetor.y

u = Vetor(1,3)
v = Vetor(3,5)

print(u.x) # 1
print(u.y) # 3

u.add(v)

print(u.x) # 4
print(u.y) # 8

u.sub(v)

print(u.x) # 4
print(u.y) # 8

