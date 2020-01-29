from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistacontaprovisaosaldo = Arquivolista('/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                                          'ContaProvisaoSaldo')
listacontaprovisaosaldo = arqlistacontaprovisaosaldo.ler()
listanova = []
for x in listacontaprovisaosaldo:
    registro = {'nome': x['nome'], 'saldoini': x['saldo'], 'mes': x['mes'], 'ano': x['ano'],
                'realizado': 0, 'saldofim': 0}
    listanova.append(registro.copy())
    print(f'CONTA {x["nome"]} INSERIDA')

print(listanova)
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistacontaprovisaosaldo.gravar(listanova)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
