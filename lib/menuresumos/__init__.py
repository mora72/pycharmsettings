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
    totaldespesas = 0
    totalreceitas = 0
    totalemprestimos = 0
    tipoconta = ''
    gastoreal = 0
    cabecalho('RECEITAS')
    for c, x in enumerate(listaresumo):
        if c % 3 == 0 or c == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            if tipoconta == 'R':
                print(f'{x:<30} ', end="")
        elif (c-1) % 3 == 0 or (c-1) == 0:
            if tipoconta == 'R':
                gastoreal = x
                print(f'{x:>10,.2f} ', end="")
                totalreceitas += x
        else:
            if tipoconta == 'R':
                gastoprev = x
                vlrdelta = gastoreal - gastoprev
                print(f'{gastoprev:>10,.2f} {vlrdelta:>10,.2f}')
    print(linha())
    print(f'TOTAL RECEITAS: {totalreceitas:>8.2f}')

    cabecalho('DESPESAS')
    for c, x in enumerate(listaresumo):
        if c % 3 == 0 or c == 0:
            tipoconta = list(filter(lambda conta: conta["nome"] == x, listacontas))[0]["tipo"]
            if tipoconta in ('D', 'E'):
                print(f'{x:<30} ', end="")
        elif (c-1) % 3 == 0 or (c-1) == 0:
            if tipoconta in ('D', 'E'):
                gastoreal = x
                print(f'{x:>10,.2f} ', end="")
                if tipoconta == 'D':
                    totaldespesas += x
                elif tipoconta == 'E':
                    totalemprestimos += x
        else:
            if tipoconta in ('D', 'E'):
                gastoprev = x
                vlrdelta = gastoreal - gastoprev
                print(f'{gastoprev:>10,.2f} {vlrdelta:>10,.2f}')
    print(linha())
    print(f'TOTAL DESPESAS: {totaldespesas:>8.2f}')
    print(f'TOTAL EMPRÉSTIMOS: {totalemprestimos:>8.2f}')
    aguardaenter()
