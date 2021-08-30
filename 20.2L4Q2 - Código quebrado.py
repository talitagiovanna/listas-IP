def fatoracao(numero):
    variavel = numero
    fatores = []
    d = 2
    while variavel > 1:
        if variavel % d == 0:
            variavel = variavel / d
            fatores.append(d)
        else:
            d += 1
    return fatores


n_linhas = int(input())
decomposicao = []
length = 1000000000
n = 0

for i in range(n_linhas):
    f = int(input())
    aux = fatoracao(f)
    b = aux
    if len(aux) < length:
        length = len(aux)
        decomposicao = aux
        n = i + 1
print(f"Iremos pela linha {n}")

lista_dec = []
for a in decomposicao:
    if a not in lista_dec:
        lista_dec.append(a)
a = 0
for d in lista_dec:
    a = decomposicao.count(d)
    print(a)