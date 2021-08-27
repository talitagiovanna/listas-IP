Finn = int(input())
Jake = int(input())
Princesacaroco = int(input())
Bmo = int(input())
Condedelimao = int(input())
maior = Princesacaroco
Vencedor = "Princesa Caroço"

if Jake >= maior:
    maior = Jake
    Vencedor = "Jake"
if Finn >= maior:
    maior = Finn
    Vencedor = "Finn"
if Condedelimao >= maior:
    maior = Condedelimao
    Vencedor = "Conde de Limão"
if Bmo >= maior:
    maior = Bmo
    Vencedor = "BMO"

print(f"{Vencedor} ganha com {maior} pontos!")