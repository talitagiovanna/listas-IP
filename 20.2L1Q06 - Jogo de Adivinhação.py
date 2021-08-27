B = int(input())
F = int(input())
Ja = int(input())
M = int(input())
Ju = int(input())
# diferenças
Df = abs(B - F)
Dja = abs(B - Ja)
Dm = abs(B - M)
Dju = abs(B - Ju)

menor = 101
nome = ""

if Df < menor:
    if Df == 0:
        print("Finn acertou em cheio!")
        Dja, Dm, Dju = 101
    else:
        nome = "Finn"
    menor = Df
if Dja < menor:
    if Dja == 0:
        print("Jake acertou em cheio!")
        Dm, Dju = 101
    else:
        nome = "Jake"
    menor = Dja
if Dm < menor:
    if Dm == 0:
        print("Marceline acertou em cheio!")
        Dju = 101
    else:
        nome = "Marceline"
    menor = Dm
if Dju < menor:
    if Dju == 0:
        print("Jujuba acertou em cheio!")
    else:
        nome = "Jujuba"
    menor = Dju
if menor > 20:
    print("Nenhum de voces chegou perto! BMO venceu!")
elif menor != 0:
    print(f"{nome} venceu! com uma diferenca de {menor}.")