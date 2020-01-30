# Funções do Menu INVESTIMENTOS
from lib.interface import *


def newinvest(lista, mestrabalho, anotrabalho):
    system("cls")
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
