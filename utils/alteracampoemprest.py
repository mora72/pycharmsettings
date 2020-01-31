from sys import path
from lib.arquivos import *
from lib.interface import aguardaenter
path.append('C:/Users/carlo/PycharmProjects/fc)')

arqlistatrans = Arquivolista('/Users/carlo/PycharmProjects/fc/basetrans.pck1', 'Transações')
listatrans = arqlistatrans.ler()

listatrans[12]['nomeemprest'] = 'PerimTok'
listatrans[54]['nomeemprest'] = 'Artur100'
listatrans[58]['nomeemprest'] = 'Mãe150'
listatrans[62]['nomeemprest'] = 'CaféTok'
listatrans[81]['nomeemprest'] = 'ReembViviane'
listatrans[126]['nomeemprest'] = 'Provisão'
print(listatrans[12])
print(listatrans[54])
print(listatrans[58])
print(listatrans[62])
print(listatrans[81])
print(listatrans[126])
opcao = int(input('Digite 1 para confirmar ou 2 para abortar'))
if opcao == 1:
    arqlistatrans.gravar(listatrans)
    print('FEITO')
else:
    print('ABORTADO')
aguardaenter()
