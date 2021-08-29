numero_de_oponentes = int(input())
media_universal_de_vida = int(input())
nao_derrotados = 0
for i in range(numero_de_oponentes):
    nome_do_oponente = input()
    vida_do_oponente = int(input())
    num_ataques_sofrido = int(input())
    A = 0
    porcentagem = vida_do_oponente*100/media_universal_de_vida
    if porcentagem < 50:
        planeta_de_origem = "Asgard"
    elif 50 <= porcentagem <= 80:
        planeta_de_origem = "Xandar"
    elif 80 < porcentagem < 120:
        planeta_de_origem = "Sakaar"
    elif 120 <= porcentagem <= 150:
        planeta_de_origem = "Vormir"
    else:
        planeta_de_origem = "Ego"
    for c in range(num_ataques_sofrido):
        D = int(input())
        A += D
    if A >= vida_do_oponente:
        print(f"{nome_do_oponente} do planeta {planeta_de_origem} foi derrotado!")
    else:
        nao_derrotados +=1
        print(f"{nome_do_oponente}, do planeta {planeta_de_origem}, conseguiu escapar.")
if nao_derrotados != 0:
    print("Alguns oponentes ainda estao a espreita...")
else:
    print("Conseguimos deixar a galaxia segura.")