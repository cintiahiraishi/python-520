
class Usuario:

    id = 1
    nome = 'Cintia Hiraishi Marsola'
    idade = 26

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

#usuario = Usuario()
usuario = Usuario(id=1, nome='Lucas',idade=26)
usuario_2 = Usuario (id=2, nome='Cory',idade=0)

print(usuario.id)
print(usuario.nome)
print(usuario.idade)



