X = float(input())
porcentagem = 0
try:
    print(f"Acompanhamento de progresso de voo inicializado, nossa altitude atual é {X} pés")
    while X < 85000:
        A = float(input())
        porcentagem = ((A+X)*100)/85000
        X +=A
        Y = ""
        if porcentagem  < 50:
            Y = "temos um longo caminho pela frente!"
        elif 50 <= porcentagem <= 70:
            Y = "tô sentindo um friozinho na barriga, Sr!"
        elif 70 < porcentagem < 100:
            Y = "ESTAMOS QUASE LÁ!"
        else:
            Y = "novo recorde de altitude estabelecido, Sr!"
        print(f"Sr Stark, {round(porcentagem, 2)}% da altitude recorde foi percorrida, {Y}")
except:
    if porcentagem < 100:
        print(f"Sr Stark, conseguimos voar apenas {round(porcentagem, 2)}% da altitude recorde, mas quem sabe na próxima conseguimos.")