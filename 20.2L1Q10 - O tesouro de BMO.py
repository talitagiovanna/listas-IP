import math
I1 = input()
I2 = input()
I3 = input()
I4 = input()
dinheiro = 0
qtdeaventuras = 0

if I1 == "Coroa":
    dinheiro += 100
if I2 == "Moedas":
    dinheiro += 200
if I3 == "Ouro Puro":
    dinheiro += 500
if I4 == "Joias":
    dinheiro += 1000
if I1 == "Moedas":
    dinheiro += 200
if I2 == "Ouro Puro":
    dinheiro += 500
if I3 == "Joias":
    dinheiro += 1000
if I4 == "Coroa":
    dinheiro += 100
if I1 == "Ouro Puro":
    dinheiro += 500
if I2 == "Joias":
    dinheiro += 1000
if I3 == "Coroa":
    dinheiro += 100
if I4 == "Moedas":
    dinheiro += 200
if I1 == "Joias":
    dinheiro += 1000
if I2 == "Coroa":
    dinheiro += 100
if I3 == "Moedas":
    dinheiro += 200
if I4 == "Ouro Puro":
    dinheiro += 500
if dinheiro == 1800:
    print("Sorte Grande! Parece que Finn e Jake conseguirao fazer uma aventura com o dinheiro arrecadado, apesar de nao ser muito, a diversao continua.")
if dinheiro < 1800:
    a = 1800 - dinheiro
    if a <= 500:
        print(f"Mas que pena, os aventureiros nao conseguiram o valor necessario para suas aventuras e terao de trabalhar um pouco para conseguir os R${a} restantes.")
    elif a > 500:
        print(f"Aparentemente a sorte nao estava ao nosso lado, apesar das expectativas ainda faltam R${a} para o objetivo e a dupla tera de passar mais uma temporada sem aventuras.")
if dinheiro > 1800:
    b = dinheiro - 1800
    qtdeaventuras = math.floor(dinheiro/1800)
    print(f"Uhuulll, conseguimos bancar {qtdeaventuras} aventura(s) e ainda sobrou R${b} para as guloseimas.")