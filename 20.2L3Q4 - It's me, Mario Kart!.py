#lista com nome dos corredores e suas respectivas posições
corredor = []
posicao = []

#inserir nas variável os inputs
for i in range(8):
    corredor_posicao = input()
    corredor.append(corredor_posicao.split()[0])
    posicao.append(corredor_posicao.split()[1])

#tamanho da lista
n = len(posicao)

#bublesort para ordenar as posições e corredores
for j in range(n-1):
    for a in range(n-1):
        if posicao[a] > posicao[a + 1]:
            aux = posicao[a]
            posicao[a] = posicao[a + 1]
            posicao[a + 1] = aux

            aux_c = corredor[a]
            corredor[a] = corredor[a + 1]
            corredor[a + 1] = aux_c

print(f"Corredor - Posicao\n{corredor[0]} - {posicao[0]}\n{corredor[1]} - {posicao[1]}\n{corredor[2]} - {posicao[2]}\n{corredor[3]} - {posicao[3]}\n{corredor[4]} - {posicao[4]}\n{corredor[5]} - {posicao[5]}\n{corredor[6]} - {posicao[6]}\n{corredor[7]} - {posicao[7]}")