
def calcular_media(lista):
    return sum(lista) / len(lista)

def encontrar_maior_numero(lista):
    return max(lista)


#def multiplicar_por_dois(x):
#    return x*2

#def multiplicar_tudo_por_dois(lista):
#    return list (map(multiplicar_tudo_por_dois, lista))

def multiplicar_tudo_por_dez(lista):
    return list (map(lambda x: x*10, lista))

lista_1 = [1,2,3,4,5]

print(lista_1)
lista_2 = multiplicar_tudo_por_dez(lista_1)
print(lista_2)

def mul_dois_v1(lista):
    nova_lista = []
    for numero in lista:
        nova_lista.append(mul_dois(numero))
    return nova_lista

def mul_dois_v2(lista):
    return list(map(mul_dois,lista))

def mul_dois_v3(lista):
    return list(map(lambda x: x*2, lista))

#
def mul_dois(x):
    return x * 2

def mul_dois_v1(lista):
    nova_lista = []
    for numero in lista:
        nova_lista.append(mul_dois(numero))
    return nova_lista

def mul_dois_v2(lista):
    return list(map(mul_dois, lista))

def mul_dois_v3(lista):
    return list(map(lambda x: x * 2, lista))




lista = [ 1, 2, 3, 4 ]

lista_v1 = mul_dois_v1(lista)
lista_v2 = mul_dois_v2(lista)
lista_v3 = mul_dois_v3(lista)

print(lista_v1)
print(lista_v2)
print(lista_v3)
