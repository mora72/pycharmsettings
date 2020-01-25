# Funções do Menu SETUP
# from os import system
from lib.interface import *


def cadmeios(lista):
    system("cls")
    cabecalho('Cadastro de Meios de Transação')
    codmeio = input('Digite código do Meio de Transação (2 letras): ')
    nomemeio = input('Digite o nome do Meio de Transacao: ')
    while True:
        tipomeio = input('Digite tipo do Meio de Transação (CC - Conta Corrente; DI - Dinheiro; CA - Cartão): ')
        if tipomeio in ('CC', 'cc', 'DI', 'di', 'CA', 'ca'):
            break
        print('Tipo Inválido !')
    registromeio = {'cod': codmeio, 'nome': nomemeio, 'tipo': tipomeio}
    lista.append(registromeio.copy())
    print('REGISTRO INSERIDO')
    aguardaenter()


def exibemeios(lista):
    system("cls")
    cabecalho('MEIOS DE TRANSAÇÃO CADASTRADOS')
    for x in lista:
        print(f'{x["cod"]} - {x["nome"]:<20} - {x["tipo"]}')
    aguardaenter()


def deletameio(lista):
    system("cls")
    cabecalho('Deletar Meio de Transação Financeira')
    codmeiotransacao = input('Digite código do Meio de Transação (2 letras) que deseja deletar: ')
    achou = False
    posregistro = -1
    nomemeiotransacao = ''
    tipomeio = ''
    for c, x in enumerate(lista):
        if x["cod"] == codmeiotransacao:
            achou = True
            nomemeiotransacao = x["nome"]
            tipomeio = x["tipo"]
            posregistro = c
            break
    if achou:
        print(f'Registro código: {codmeiotransacao}, nome: {nomemeiotransacao}, tipo: {tipomeio} DELETADO !')
        del lista[posregistro]
    else:
        print(f'Registro código: {codmeiotransacao} não encontrado!')
    aguardaenter()


def cadcontas(lista):
    while True:
        system("cls")
        cabecalho('Cadastro de tipos de conta de receita ou despesa')
        nomeconta = input('Digite o nome da conta de receita ou despesa ou "Sair" para SAIR : ')
        if nomeconta in ('Sair', 'SAIR', 'sair'):
            break
        tipoconta = input('Digite o tipo da conta (R = Receita; D = Despesa; '
                          'T = Transferência; E = Empréstimo; C = PagtoCartão: ').upper()
        registroconta = {'nome': nomeconta, 'tipo': tipoconta}
        lista.append(registroconta.copy())
        print('REGISTRO INSERIDO')
        aguardaenter()


def deletaconta(lista):
    system("cls")
    cabecalho('Deletar Conta de Receita ou Despesa')
    nomeconta = input('Digite nome da conta que deseja deletar: ')
    achou = False
    posregistro = -1
    for c, x in enumerate(lista):
        if x["nome"] == nomeconta:
            achou = True
            posregistro = c
            break
    if achou:
        print(f'Registro nome: {nomeconta} DELETADO !')
        del lista[posregistro]
    else:
        print(f'Registro nome: {nomeconta} não encontrado!')
    aguardaenter()


def alteramesanotrabalho():
    system("cls")
    cabecalho('Alteração do Ano e/ou Mes de Trabalho')
    ano = leiaint('Digite ano de trabalho: ')
    mes = leiaint('Digite mes de trabalho: ')
    print('OK. Alterado.')
    aguardaenter()
    return ano, mes


def meiossaldo(listameios, listameiossaldo, mestrabalho, anotrabalho):
    while True:
        system("cls")
        cabecalho('SALDO DE CONTAS CORRENTE')
        for x in listameiossaldo:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                print(f'{x["cod"]} - {x["saldo"]}')
        linha()
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar ou 9 - Sair: ')
        if opcao == 1:
            codmeio = leiameio('Digite código do meio: ', listameios)
            saldomeio = leiafloat('Digite o saldo do meio: ')
            registro = {'cod': codmeio, 'saldo': saldomeio, 'mes': mestrabalho, 'ano': anotrabalho}
            listameiossaldo.append(registro.copy())
            print('REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            codmeio = leiameio('Digite código do meio: ', listameios)
            for c, x in enumerate(listameiossaldo):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["cod"] == codmeio:
                    print('REGISTRO REMOVIDO !')
                    del listameiossaldo[c]
                    aguardaenter()
                    break
        elif opcao == 9:
            break


def contasprevisto(listacontas, listacontasprevisto, mestrabalho, anotrabalho):
    while True:
        system("cls")
        cabecalho('PREVISÃO DE GASTOS POR CONTA')
        for x in listacontasprevisto:
            if x["mes"] == mestrabalho and x["ano"] == anotrabalho:
                print(f'{x["nome"]} - {x["valorprevisto"]}')
        linha()
        opcao = leiaint('Digite 1 - Cadastrar; 2 - Deletar ou 9 - Sair: ')
        if opcao == 1:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            valorprevisto = leiafloat('Digite o valor previsto: ')
            registro = {'nome': nomeconta, 'valorprevisto': valorprevisto, 'mes': mestrabalho, 'ano': anotrabalho}
            listacontasprevisto.append(registro.copy())
            print('REGISTRO INSERIDO')
            aguardaenter()
        elif opcao == 2:
            nomeconta = leiaconta('Digite nome da conta: ', listacontas)
            for c, x in enumerate(listacontasprevisto):
                if x["mes"] == mestrabalho and x["ano"] == anotrabalho and x["nome"] == nomeconta:
                    print('REGISTRO REMOVIDO !')
                    del listacontasprevisto[c]
                    aguardaenter()
                    break
        elif opcao == 9:
            break
