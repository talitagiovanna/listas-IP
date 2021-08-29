nome_especie = input()
quantidade_1 = 0

while True:
    nome_1 = input()

    if nome_1 == "fim":
        break

    nome_2 = input()
    caracteristica_1 = input()
    caracteristica_2 = input()
    probabilidade_1 = int(input())
    probabilidade_2 = int(input())
    potencial_1 = int(input())
    potencial_2 = int(input())

    especie_1 = (probabilidade_1 - potencial_1)**2
    especie_2 = (probabilidade_2 - potencial_2)**2

    if especie_1 > especie_2:
        print(f"O bebê ET gerado é da espécie {nome_1} e tem como característica {caracteristica_1}")
        quantidade_1 += 1
    else:
        print(f"O bebê ET gerado é da espécie {nome_2} e tem como característica {caracteristica_2}")
print(f"nasceram {quantidade_1} bebês ETs da espécie {nome_especie}")