from lib.interface import *


def resumomes(listatrans, mestrabalho, anotrabalho, listacontas, listacontasprevisto):
    print('')
    listaresumo = []
    listacontasord = sorted(listacontas, key=lambda i: i['nome'])
    for x in listacontasord:
        listaresumo.append(x['nome'])
        listaresumo.append(float(0))
        vlrprevtemp = list(filter(lambda conta: conta['nome'] == x['nome'], listacontasprevisto))
        if len(vlrprevtemp) > 0:
            vlrprev = vlrprevtemp[0]['valorprevisto']
        else:
            vlrprev = 0
        listaresumo.append(vlrprev)
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
    gastoreal = 0
    for c, x in enumerate(listaresumo):
        if c % 3 == 0 or c == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            print(f'{x:<30} ', end="")
        elif (c-1) % 3 == 0 or (c-1) == 0:
            gastoreal = x
            print(f'{x:>10,.2f} ', end="")
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
        else:
            gastoprev = x
            vlrdelta = gastoreal - gastoprev
            print(f'{gastoprev:>10,.2f} {vlrdelta:>10,.2f}')
    print(linha())
    print(f'TOTAL GERAL: {totalgeral:>8.2f}')
    print(f'TOTAL DESPESAS: {totaldespesas:>8.2f}')
    print(f'TOTAL RECEITAS: {totalreceitas:>8.2f}')
    print(f'TOTAL TRANSFERÊNCIAS: {totaltransf:>8.2f}')
    print(f'TOTAL EMPRÉSTIMOS: {totalemprestimos:>8.2f}')
    print(f'TOTAL CARTÃO: {totalcartao:>8.2f}')
    print(f'TOTAL OUTROS: {totaloutros:>8.2f}')
    aguardaenter()
