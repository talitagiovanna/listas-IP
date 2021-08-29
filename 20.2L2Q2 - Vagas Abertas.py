heroi_1 = input()
heroi_2 = input()
heroi_3 = input()

pontuacao_1 = 0
pontuacao_2 = 0
pontuacao_3 = 0
fim = True

while fim:
    acao_1 = input()
    acao_2 = input()
    acao_3 = input()

    if acao_1 == "Derrotar capangas":
        pontuacao_1 += 5
    if acao_2 == "Derrotar capangas":
        pontuacao_2 += 5
    if acao_3 == "Derrotar capangas":
        pontuacao_3 += 5
    if acao_1 == "Salvar civis":
        pontuacao_1 += 20
    if acao_2 == "Salvar civis":
        pontuacao_2 += 20
    if acao_3 == "Salvar civis":
        pontuacao_3 += 20
    if acao_1 == "Destruir propriedade alheia":
        pontuacao_1 -= 10
    if acao_2 == "Destruir propriedade alheia":
        pontuacao_2 -= 10
    if acao_3 == "Destruir propriedade alheia":
        pontuacao_3 -= 10
    if acao_1 == "Derrotar o vilao":
        pontuacao_1 += 50
        fim = False
    if acao_2 == "Derrotar o vilao":
        pontuacao_2 += 50
        fim = False
    if acao_3 == "Derrotar o vilao":
        pontuacao_3 += 50
        fim = False
if pontuacao_1 >= pontuacao_2 and pontuacao_1 >= pontuacao_3:
    print(f"{heroi_1} saiu da simulacao com {pontuacao_1}pts e se tornou o(a) mais novo(a) integrante dos Vingadores!")
elif pontuacao_2 > pontuacao_1 and pontuacao_2 >= pontuacao_3:
    print(f"{heroi_2} saiu da simulacao com {pontuacao_2}pts e se tornou o(a) mais novo(a) integrante dos Vingadores!")
elif pontuacao_3 > pontuacao_1 and pontuacao_3 > pontuacao_2:
    print(f"{heroi_3} saiu da simulacao com {pontuacao_3}pts e se tornou o(a) mais novo(a) integrante dos Vingadores!")