#https://github.com/LucasRicciardi/python-520
lista_de_nomes = []

def imprimir_menu():
    print('Selecione uma das opções abaixo: ')
    print('\t 1. Adicionar nome ao sorteio')
    print('\t 2. Zerar lista de sorteio')
    print('\t 3. Ver lista de sorteio')
    print('\t 4. Sortear')
    print('\t 5. Sair')

def adicionar_nome_ao_sorteio():
    pass

def zerar_lista_de_sorteio():
    pass

def ver_lista_de_sorteio():
    pass

def sortear():
    pass

def sair():
    pass

done = False
while not done:
    imprimir_menu()
    opcao = input('Digite a opção escolhida: ')    
    if opcao == '1':
        adicionar_nome_ao_sorteio()
    elif opcao == '2':
        zerar_lista_de_sorteio()
    elif opcao == '3':
        ver_lista_de_sorteio()
    elif opcao == '4':
        sortear()
    elif opcao == '5':
        sair()
    else:
        print('Opção inválida')