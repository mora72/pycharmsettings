# Funções do Menu INVESTIMENTOS
from lib.interface import *


def newinvest(lista, mestrabalho, anotrabalho):
    exibeinvest(lista, mestrabalho, anotrabalho)
    cabecalho(f'ANO TRABALHO: {anotrabalho} - MES TRABALHO: {mestrabalho}')
    cabecalho('NOVO INVESTIMENTO')
    while True:
        tipoinvest = input('Digite o tipo do investimento: ')
        nomeinvest = input('Digite o nome do investimento: ')
        diainiinvest = leiaint('Digite o dia do início do investimento: ')
        mesiniinvest = leiaint('Digite o mês do início do investimento: ')
        anoiniinvest = leiaint('Digite o ano do início do investimento: ')
        qtdeini = leiaint('Digite quantidade inicial: ')
        vlruniini = leiafloat('Digite valor unitário inicial: ')
        vlrtotini = vlruniini * qtdeini
        cabecalho('CONFIRMA REGISTRO ? ')
        opcao = input('Sim (S) ou Não (N) ? ')
        if opcao in 'Ss':
            registro = {'ano': anotrabalho,
                        'mes': mestrabalho,
                        'diainiinvest': diainiinvest,
                        'mesiniinvest': mesiniinvest,
                        'anoiniinvest': anoiniinvest,
                        'tipoinvest': tipoinvest,
                        'nomeinvest': nomeinvest,
                        'vlruniini': vlruniini,
                        'qtdeini': qtdeini,
                        'vlrtotini': vlrtotini,
                        'qtdefim': 0,
                        'vlrunifim': 0,
                        'vlrtotfim': 0,
                        }
            lista.append(registro.copy())
            print('REGISTRO INSERIDO')
        opcao = input('Lançar outra transação? Sim (S) ou Não (N) ? ')
        if opcao in 'Nn':
            break


def exibeinvest(lista, mes, ano):
    system("cls")
    cabecalho('INVESTIMENTOS DO MES E ANO DE TRABALHO')
    opcao = leiaint('Digite 1 para ver todos ou 2 para um tipo específico: ')
    if opcao == 1:
        tipoinvest = '*'
    elif opcao == 2:
        tipoinvest = input('Digite o tipo do investimento: ')
    else:
        tipoinvest = ''
    for c, x in enumerate(lista):
        if x["mes"] == mes and x["ano"] == ano and (x["tipoinvest"] == tipoinvest or tipoinvest == '*'):
            print(f'ID: {c:3} - {x["diainiinvest"]:2}/{x["mesiniinvest"]:2}/{x["anoiniinvest"]} '
                  f'{x["tipoinvest"]:<20} {x["nomeinvest"]:<20} '
                  f'{x["vlruniini"]:>10,.2f} {x["qtdeini"]:>4} {x["vlrtotini"]:>10,.2f} '
                  f'{x["vlrunifim"]:>10,.2f} {x["qtdefim"]:>4} {x["vlrtotfim"]:>10,.2f} ')
    aguardaenter()


def deletainvest(lista, mes, ano):
    exibeinvest(lista, mes, ano)
    cabecalho('Deletar Investimento')
    while True:
        idtransacao = leiaint('Digite ID do Investimento que deseja deletar ou -1 para desistir: ')
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


def updateinvest(lista, mes, ano):
    exibeinvest(lista, mes, ano)
    cabecalho('Atualizar Investimento')
    while True:
        while True:
            idtrans = leiaint('Digite ID do Investimento que deseja deletar ou -1 para desistir: ')
            if -1 <= idtrans <= len(lista) - 1:
                break
            else:
                print('ID Inválido !')
        if idtrans >= 0:
            lista[idtrans]["vlrunifim"] = leiafloat('Digite novo valor unitário final: ')
            lista[idtrans]["qtdefim"] = leiaint('Digite nova qtde final: ')
            lista[idtrans]["vlrtotfim"] = lista[idtrans]["vlrunifim"] * lista[idtrans]["qtdefim"]
            print(f'ID ALTERADO !')
            aguardaenter()
        else:
            print('Alteração CANCELADA !')
            aguardaenter()
            break
