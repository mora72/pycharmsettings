# Funções do Menu TRANSACOES
# from os import system
from lib.interface import *


def lanctrans(lista, anotrabalho, mestrabalho, listameios, listacontas):
    system("cls")
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    cabecalho('Lançamento de Transações')
    meiotrans = leiameio('Digite o meio desta transação: ', listameios)
    while True:
        cabecalho(f'NOVO REGISTRO DO MEIO: {meiotrans}')
        diatrans = leiadia('Digite o dia da transação: ', mestrabalho, anotrabalho)
        valortrans = leiafloat('Digite o valor da transação: ')
        contatrans = leiaconta('Digite a conta da transação: ', listacontas)
        descrtrans = input('Digite uma descrição para esta transação: ')
        if descrtrans == '':
            descrtrans = contatrans
        cabecalho('CONFIRMA REGISTRO ? ')
        print(f'data...: {diatrans:2}/{mestrabalho:2}/{anotrabalho}')
        print(f'meio..: {meiotrans}')
        print(f'conta.: {contatrans}')
        print(f'valor.: {valortrans}')
        print(f'descrição...: {descrtrans}')
        opcao = input('Sim (S) ou Não (N) ? ')
        if opcao in 'Ss':
            registrotrans = {'ano': anotrabalho,
                             'mes': mestrabalho,
                             'dia': diatrans,
                             'valor': valortrans,
                             'conta': contatrans,
                             'descr': descrtrans,
                             'meio': meiotrans}
            lista.append(registrotrans.copy())
            print('REGISTRO INSERIDO')
        opcao = input('Lançar outra transação? Sim (S) ou Não (N) ? ')
        if opcao in 'Nn':
            break


def exibetrans(lista):
    system("cls")
    cabecalho('LANCAMENTOS DO MES E ANO DE TRABALHO')
    for c, x in enumerate(lista):
        print(f'ID: {c:2} - {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} - ', end='')
        print(f'{x["valor"]:>10.2f} - {x["conta"]:<20} - {x["descr"]:<50} - {x["meio"]}')
    aguardaenter()


def exibetransmeiosaldo(listatrans, listameios, listameiossaldo, mestrabalho, anotrabalho):
    system("cls")
    cabecalho('LANCAMENTOS E SALDO DE UM MEIO')
    codmeio = leiameio('Digite código do meio: ', listameios)
    saldo = 0
    for x in listameiossaldo:
        if x["cod"] == codmeio and x["ano"] == anotrabalho and x["mes"] == mestrabalho:
            saldo = x["saldo"]
            break
    for c, x in enumerate(listatrans):
        if x["meio"] == codmeio:
            saldo = saldo + x["valor"]
            print(f'ID: {c:2} - {x["dia"]:2}/{x["mes"]:2}/{x["ano"]} - ', end='')
            print(f'{x["valor"]:>8.2f} - {x["conta"]:<20} - {x["descr"]:<30} - {x["meio"]} - saldo: {saldo:>9.2f}')
    aguardaenter()


def deletatrans(lista):
    exibetrans(lista)
    cabecalho('Deletar Meio de Transação Financeira')
    while True:
        idtransacao = leiaint('Digite ID da Transação que deseja deletar ou -1 para desistir: ')
        if -1 <= idtransacao <= len(lista) - 1:
            break
        else:
            print('ID Inválido !')
    if idtransacao >= 0:
        print(f'ID DELETADO !')
        del lista[idtransacao]
    else:
        print('Deleção CANCELADA !')
    aguardaenter()
