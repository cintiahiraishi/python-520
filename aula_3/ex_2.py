
def calcular_media(lista_de_notas):
    resultado = 0
    contador = 0
    for nota in lista_de_notas:
        resultado = resultado + nota
        contador = contador + 1
    return resultado / contador






#lista_de_notas = [6, 4, 1, 8, 8, 10, 1]
precos_das_laranjas = [ 6, 4, 1, 8, 8, 10, 1, 7 ]
media = calcular_media (precos_das_laranjas)

print(media)