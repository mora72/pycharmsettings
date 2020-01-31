from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
listatrans = arqlistatrans.ler()
print(listatrans[0])
print(listatrans[1])
print(listatrans[2])
print(listatrans[3])
print(len(listatrans))
listanova = []
for c, x in enumerate(listatrans):
    x['nomeemprest'] = ''
    listanova.append(x.copy())
    print(f'REG {c} INSERIDO')

print(listanova[0])
print(listanova[1])
print(listanova[2])
print(listanova[3])
print(len(listanova))
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistatrans.gravar(listanova)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
