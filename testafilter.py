from lib.arquivos.bacarquivos import *

listacontas = lerarqcontas()
print(listacontas)
print(list(filter(lambda conta: conta["nome"] == "Aluguel Guilherme", listacontas)))
listares = list(filter(lambda conta: (conta["nome"] == "Aluguel Guilherme" and conta["tipo"] == "R"), listacontas))
print(listares[0]["tipo"])
