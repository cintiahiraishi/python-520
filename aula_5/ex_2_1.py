
class Usuario:

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.esta_habilitado = True if idade > 18 else False

    def nascer(self):
        self.idade = 0

    def envelhecer(self):
        self.idade = self.idade + 1

    def tirar_habilitacao(self):
        if self.idade > 17:
            self.esta_habilitado = True
            #print('Estou habilitado!')
        else:
            self.esta_habilitado = False
            #print('Ainda faltam ' + str(18 -self.idade) + 'anos')

usuario = Usuario(1, 'José', 10)

while usuario.idade < 18:
    usuario.envelhecer()
    usuario.tirar_habilitacao()

print(usuario.esta_habilitado)

