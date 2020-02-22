
class ContaBancaria:

    def __init__(self, cliente):
        self.saldo = 0.0
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor 

    def render(self):
        self.saldo *= 1.01

def simular(conta_bancaria):
    conta_bancaria.depositar(100.00)
    for i in range(12):
        conta_bancaria.render()
    conta_bancaria.sacar(110.00)
    print(conta_bancaria.saldo)

conta_bancaria = ContaBancaria('Lucas')

simular(conta_bancaria)