
email = input ('Digite seu e-mail: ')
caracter = ['@'] 
contador = 0
quantidade = 0

for letra in email:
    if letra in caracter:
        contador = (contador + 1)
if contador ==1:
    print ('Digitou um e-mail valido')
else:
    print ('Nao digitou um e-mail')
