#lista com nomes de acordo com suas posições
posicao = []
#loop para adicionar os nomes dos 14 magos de acordo com suas posições
for i in range(14):
    posicao.append(input())
#guardando o mago que ficou em primeiro no ínicio da corrida
primeiro = [posicao[0]]

#números de ações de cada jogador
N = int(input())
#nome dos jogadores e suas ações
jogadores_acao = []

#separar nome dos magos e ação
for a in range(N):
    jogadores_acao = input().split()
    #vendo se a ação é negativa
    if jogadores_acao[1] == "caiu" or jogadores_acao[1] == "falta":
        index = posicao.index(jogadores_acao[0])
        if index == 13:
            posicao[index] = posicao[13]
        else:
            temp = posicao[index + 1]
            posicao[index + 1] = posicao[index]
            posicao[index] = temp
    #vendo se a ação é positiva
    if jogadores_acao[1] == "captura" or jogadores_acao[1] == "recuperou":
        index = posicao.index(jogadores_acao[0])
        if index == 0:
            posicao[index] = posicao[0]
        else:
            temp = posicao[index - 1]
            posicao[index - 1] = posicao[index]
            posicao[index] = temp

#comparando se o primeiro no início da corrida continua no primeiro lugar ou não
if posicao[0] == primeiro[0]:
    print(f"O(a) bruxo(a) {posicao[0]} foi exemplar durante a partida e mostrou a todos que o quadribol e mais que um esporte. Ja o {posicao[-1]}, foi incapaz de fazer uma bela partida e sera rebaixado para a segunda divisao dos magos.")
else:
    print(f"Tivemos uma partida extremamente intensa e o(a) bruxo(a) {posicao[0]} se mostrou superior e conquistou a primeira colocacao, ja o(a) bruxo(a) {posicao[-1]} fez uma pessima partida e sera rebaixado para a segunda divisao dos magos.")