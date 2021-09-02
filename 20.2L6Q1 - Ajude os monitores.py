# número de sugestões recebidas
N = int(input())

#chave: tema e suas respectivas quantidade de votos
tema_voto = dict()

#loop para adicionar chaves e items
for i in range(N):
    tema_voto_1 = input().split()
    tema = tema_voto_1[0]
    voto = tema_voto_1[1]
    tema_voto[tema] = voto


lista = list()
for key in tema_voto.keys():
    lista.append(key)

#bubblesort para ordenar uma lista
def ordenar(alist, dicionario):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if int(dicionario[alist[i]])<int(dicionario[alist[i+1]]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            elif int(dicionario[alist[i]]) == int(dicionario[alist[i+1]]):
                alist[i] = alist[i]
                alist[i+1] = alist[i+1]


ordenar(lista, tema_voto)

for key in lista:
    print(f'{key} {tema_voto[key]}')
