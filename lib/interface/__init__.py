# Funções de Interface
from os import system
from datetime import date


def linha(tam=42):
    return '-' * tam


def espacos(tam=10):
    return ' ' * tam


def bordasup(tam=10):
    for c in range(1, tam):
        print('')


def cabecalho(txt, tam=42, borda=50):
    print(f'{espacos(borda)}{linha(tam)}')
    print(f'{espacos(borda)}{txt.center(tam)}')
    print(f'{espacos(borda)}{linha(tam)}')


def menu(lista, bordae=50):
    for c, x in enumerate(lista):
        print(f'{espacos(bordae)}[ {c + 1} ] - {x}')
    print(f'{espacos(bordae)}{linha()}')
    while True:
        op = leiaint(f'{espacos(bordae)}Digite sua opção: ')
        if 1 <= op <= len(lista):
            break
        else:
            print(f'{espacos(bordae)}digite opcao valida !!!')
    return op


def leiaint(msg):
    while True:
        try:
            nro = int(input(msg))
        except (TypeError, ValueError) as err:
            print(f'nro invalido! {err.args}')
        else:
            return nro


def leiafloat(msg):
    while True:
        try:
            nro = float(input(msg))
        except (ValueError, TypeError) as err:
            print(f'nro invalido! {err}')
        else:
            return nro


def aguardaenter():
    print('')
    print('DIGITE ENTER PARA CONTINUAR !')
    input('')


def exibecontas(lista):
    system("cls")
    cabecalho('CONTAS DE RECEITA OU DESPESA CADASTRADOS')
    listaord = sorted(lista, key=lambda i: (i['tipo'], i['nome']))
    for x in listaord:
        print(f'{x["nome"]:<30} - {x["tipo"]}')
    aguardaenter()


def leiaconta(msg, listacontas):
    while True:
        conta = input(msg)
        achou = False
        for x in listacontas:
            if conta == x['nome']:
                achou = True
                break
        if achou:
            break
        else:
            print('Conta não encontrada !')
            opcao = input('Digite Enter para informar novamente ou 9 para ver lista de contas: ')
            if opcao == '9':
                exibecontas(listacontas)
    return conta


def e_bisexto(ano):
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                resultado = True
            else:
                resultado = False
        else:
            resultado = True
    else:
        resultado = False
    return resultado


def leiadia(msg, mes, ano):
    while True:
        dia = leiaint(msg)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            qtdedias = 31
        elif mes == 2:
            if e_bisexto(ano):
                qtdedias = 29
            else:
                qtdedias = 28
        else:
            qtdedias = 30
        if 1 <= dia <= qtdedias:
            break
        else:
            print('Dia Incorreto !')
    return dia


def leiameio(msg, listameios):
    while True:
        meio = input(msg)
        achou = False
        for x in listameios:
            if meio == x['cod']:
                achou = True
                break
        if achou:
            break
        else:
            print('Meio não encontrado !')
            opcao = input('Digite Enter para informar novamente ou 9 para ver lista de meios: ')
            if opcao == '9':
                system("cls")
                cabecalho('MEIOS CADASTRADOS')
                for x in listameios:
                    print(f'{x["cod"]} - {x["nome"]}')
                aguardaenter()
    return meio
