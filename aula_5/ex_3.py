
class Contador:

    def __init__(self):
        self.conta = 0

    def __del__(self):
        print('hello')

    def contar(self):
        #self.conta = self.conta + 1
        self.conta += 1
        
# Código cliente
contador = Contador()
for i in range(10):
    contador.contar()
print(contador.conta)