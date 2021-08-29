#número de jogadores na sala
K = int(input())
#lista de jogadores e seus respectivos pings
jogadores = []
#lista de pings
pings = []


#inserir nome dos jogadores e pings na lista
for i in range(K):
    nome_pings = input()
    valores = nome_pings
    jogadores.append(valores.split()[0])
    pings.append(valores.split()[1])

#váriavel de maior e menor ping
maior = menor = int(pings[0][:-2])

#nome dos jogadores com maior e menor ping
jogador_maior = []
jogador_menor = []

#loop para saber quem é o maior e menor ping e seus respectivos jogadores
for index, ping in enumerate(pings):
    ping = int(ping[:-2])
    if ping > maior:
        maior = ping
        jogador_maior = []
        jogador_maior.append(jogadores[index])
    elif ping == maior:
        jogador_maior.append(jogadores[index])
    if ping < menor:
        menor = ping
        jogador_menor = []
        jogador_menor.append(jogadores[index])
    elif ping == menor:
        jogador_menor.append(jogadores[index])
print(f"O maior ping é {maior}ms, do(s) jogador(es) {', '.join(jogador_maior)}. E o menor é {menor}ms, do(s) jogador(es) {', '.join(jogador_menor)}")
