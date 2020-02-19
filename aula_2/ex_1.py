
#usuario = {
#    'nome' : input('Digite seu nome: '),
#    'idade' : input('Digite sua idade: '),
#    'n_filhos' = input('Quantos filhos você tem? '),
#    'filhos': [] 
#}

#print(usuario)


idade = input ('Digite sua idade? ')
#numerais = '0123456789'
numerais = ['0','1','2','3','4','5','6','7','8','9']

for letra in idade:
    print(letra)
    if letra in numerais:
        print ('Digitou um numero')
    else:
        print ('Digitou um caracter nao numerico')

#idade = int(idade)

