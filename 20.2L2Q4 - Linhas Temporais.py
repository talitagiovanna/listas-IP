X = int(input())
realidade_atual = 0

while True:
    try:
        y = int(input())
        i = 1
        for i in range(y + 1):
            realidade_atual += i
    except EOFError:
        if realidade_atual < X:
            print("Ainda nos falta um pouco...")
        elif realidade_atual == X:
            print("Finalmente Doutor, conseguimos!")
        elif X < realidade_atual < (X*20):
            print("Parece que o senhor passou por algumas linhas temporais a mais.")
        elif X*20 < realidade_atual < X*100:
            print("Calma, onde estamos?")
        elif realidade_atual > 100:
            print("Hum... Doutor?")
        break