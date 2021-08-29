n = int(input())

pontuacao_aranha = 0
pontuacao_rino = 0

aranha_preparo = False
rino_preparo = False

defesa_aranha = False
defesa_rino = False

defesa_1 = "Camada de teias"
preparo_1 = "É apenas uma grande massa de musculos"
ataque_1 = "Vai teia!"
defesa_2 = "Meus musculos sao macicos!"
preparo_2 = "Agora voce vai ver!"
ataque_2 = "Toma essa"

for i in range (n):
    frase_aranha = input()
    frase_rino = input()
    if frase_aranha == preparo_1:
        aranha_preparo = True
    if frase_rino == preparo_2:
        rino_preparo = True
    if frase_aranha == defesa_1:
        defesa_aranha = True
    if frase_rino == defesa_2:
        defesa_rino = True
    if frase_aranha == ataque_1 and aranha_preparo == True:
        if defesa_rino == False:
            pontuacao_aranha += 1
            print("Maldito inseto!")
        else:
            defesa_rino = False
        aranha_preparo = False
    if frase_rino == ataque_2 and rino_preparo == True:
        if defesa_aranha == False:
            pontuacao_rino += 1
            print("Droga, me descuidei")
        else:
            defesa_aranha = False
        rino_preparo = False
    defesa_rino = False
    defesa_aranha = False
if pontuacao_aranha > pontuacao_rino:
    print("Perdeu grandao!")
elif pontuacao_rino > pontuacao_aranha:
    print("Aiai apenas mais um dia comum")
else:
    print("Isso nao esta dando certo")