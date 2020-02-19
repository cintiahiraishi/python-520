
lista = [
    47,
    80,
    50,
    69,
    41,
    50,
    5,
    14,
    14,
    88,
    ]

# 1 - Descobrir se o numero e par

print (2 % 2 == 0)
print (3 % 2 == 1)

# 2 - Adicionar elementos na ista

lista = lista + [1]

print(lista)

#lista_secundaria = []

l_s = []
for numero in lista:
    if numero % 2 == 0:
        l_s = l_s + [numero * 2]
    else:
        l_s = l_s + [ numero * 3 ]
print(lista)
print(l_s)
    

