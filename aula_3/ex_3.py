
def maior_entre_dois_numeros(a,b):
    if a > b:
        return a
    return b
    #return a if a > b else b #ternario

def encontrar_o_maior_numero(lista_de_numeros):
    #pass
    maior_numero = lista_de_numeros [0]
    for numero in lista_de_numeros:
        maior_numero = maior_entre_dois_numeros(maior_numero, numero)
    return maior_numero

#def x(a,b,c,d,e):
#    m1 = maior(a,b)
#    m2 = maior (m1,c)
#    m3 = maior (m2,d)
#    m4 = maior (m3,e)


lista_de_numeros = [ 15 , 20 , 35,  8, 52 ]
maior_numero = encontrar_o_maior_numero(lista_de_numeros)

print(maior_numero)