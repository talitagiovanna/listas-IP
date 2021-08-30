from math import sqrt

def main():
    var = input().split(", ")
    quantidade_1 = 0

    for i in var:
        a = int(i)
        b = (5 * a * a) + 4
        c = (5 * a * a) - 4
        d = int(sqrt(abs(b)))
        e = int(sqrt(abs(c)))
        if (d ** 2) == b or (e ** 2) == c:
            quantidade_1 += 1
        else:
            quantidade_1 -= 1
    return quantidade_1

temp = main()
if temp == 8:
    print("Muito bom, Morty! Vamos em mais aventuras!")
elif temp == -8:
    print("Meu deus, Morty! Você precisa mesmo ir para escola!")
else:
    print("Ainda da para melhorar, Morty!")
