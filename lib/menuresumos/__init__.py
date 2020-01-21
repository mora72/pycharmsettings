from lib.interface import *


def resumomes(listatrans, mestrabalho, anotrabalho, listacontas):
    print('')
    listaresumo = []
    listacontasord = sorted(listacontas, key=lambda i: i['nome'])
    for x in listacontasord:
        listaresumo.append(x['nome'])
        listaresumo.append(float(0))
    listaresumo.index('Transf')
    for x in listatrans:
        if mestrabalho == x['mes'] and anotrabalho == x['ano']:
            pos = listaresumo.index(x['conta'])
            listaresumo[pos+1] = listaresumo[pos+1] + x['valor']
    cabecalho('RESUMO DO MES POR CONTA')
    totalgeral = 0
    totaldespesas = 0
    totalreceitas = 0
    totaltransf = 0
    totalemprestimos = 0
    totaloutros = 0
    totalcartao = 0
    tipoconta = ''
    for c, x in enumerate(listaresumo):
        if c % 2 == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            if tipoconta == 'D':
                print(f'{x:<30} - ', end='')
        else:
            if tipoconta == 'D':
                print(f'{x:>8.2f}')
            totalgeral += x
            if tipoconta == 'R':
                totalreceitas += x
            elif tipoconta == 'D':
                totaldespesas += x
            elif tipoconta == 'E':
                totalemprestimos += x
            elif tipoconta == 'T':
                totaltransf += x
            elif tipoconta == 'C':
                totalcartao += x
            else:
                totaloutros += x
    linha()
    print(f'TOTAL GERAL: {totalgeral:>8.2f}')
    print(f'TOTAL DESPESAS: {totaldespesas:>8.2f}')
    print(f'TOTAL RECEITAS: {totalreceitas:>8.2f}')
    print(f'TOTAL TRANSFERÊNCIAS: {totaltransf:>8.2f}')
    print(f'TOTAL EMPRÉSTIMOS: {totalemprestimos:>8.2f}')
    print(f'TOTAL CARTÃO: {totalcartao:>8.2f}')
    print(f'TOTAL OUTROS: {totaloutros:>8.2f}')
    aguardaenter()
