nome_1 = input()
custo_1 = float(input())
sentimental_1 = int(input())

nome_2 = input()
custo_2 = float(input())
sentimental_2 = int(input())

nome_3 = input()
custo_3 = float(input())
sentimental_3 = int(input())

nome_4 = input()
custo_4 = float(input())
sentimental_4 = int(input())

nome_5 = input()
custo_5 = float(input())
sentimental_5 = int(input())

nome_6 = input()
custo_6 = float(input())
sentimental_6 = int(input())

nome_7 = input()
custo_7 = float(input())
sentimental_7 = int(input())

nome_8 = input()
custo_8 = float(input())
sentimental_8 = int(input())

nome_9 = input()
custo_9 = float(input())
sentimental_9 = int(input())

nome_10 = input()
custo_10 = float(input())
sentimental_10 = int(input())


for i in range(1,10):
    if custo_1 < custo_2 or custo_1 == custo_2 and sentimental_1 < sentimental_2 or sentimental_1 == sentimental_2 and nome_2 > nome_1:
        aux_nome = nome_1
        aux_custo = custo_1
        aux_sentimental = sentimental_1
        nome_1 = nome_2
        custo_1 = custo_2
        sentimental_1 = sentimental_2
        nome_2 = aux_nome
        custo_2 = aux_custo
        sentimental_2 = aux_sentimental

    if custo_2 < custo_3 or custo_2 == custo_3 and sentimental_2 < sentimental_3 or sentimental_2 == sentimental_3 and nome_3 > nome_2:
        aux_nome = nome_2
        aux_custo = custo_2
        aux_sentimental = sentimental_2
        nome_2 = nome_3
        custo_2 = custo_3
        sentimental_2 = sentimental_3
        nome_3 = aux_nome
        custo_3 = aux_custo
        sentimental_3 = aux_sentimental

    if custo_3 < custo_4 or custo_3 == custo_4 and sentimental_3 < sentimental_4 or sentimental_3 == sentimental_4 and nome_4 > nome_3:
        aux_nome = nome_3
        aux_custo = custo_3
        aux_sentimental = sentimental_3
        nome_3 = nome_4
        custo_3 = custo_4
        sentimental_3 = sentimental_4
        nome_4 = aux_nome
        custo_4 = aux_custo
        sentimental_4 = aux_sentimental

    if custo_4 < custo_5 or custo_4 == custo_5 and sentimental_4 < sentimental_5 or sentimental_4 == sentimental_5 and nome_5 > nome_4:
        aux_nome = nome_4
        aux_custo = custo_4
        aux_sentimental = sentimental_4
        nome_4 = nome_5
        custo_4 = custo_5
        sentimental_4 = sentimental_5
        nome_5 = aux_nome
        custo_5 = aux_custo
        sentimental_5 = aux_sentimental

    if custo_5 < custo_6 or custo_5 == custo_6 and sentimental_5 < sentimental_6 or sentimental_5 == sentimental_6 and nome_6 > nome_5:
        aux_nome = nome_5
        aux_custo = custo_5
        aux_sentimental = sentimental_5
        nome_5 = nome_6
        custo_5 = custo_6
        sentimental_5 = sentimental_6
        nome_6 = aux_nome
        custo_6 = aux_custo
        sentimental_6 = aux_sentimental

    if custo_6 < custo_7 or custo_6 == custo_7 and sentimental_6 < sentimental_7 or sentimental_6 == sentimental_7 and nome_7 > nome_6:
        aux_nome = nome_6
        aux_custo = custo_6
        aux_sentimental = sentimental_6
        nome_6 = nome_7
        custo_6 = custo_7
        sentimental_6 = sentimental_7
        nome_7 = aux_nome
        custo_7 = aux_custo
        sentimental_7 = aux_sentimental

    if custo_7 < custo_8 or custo_7 == custo_8 and sentimental_7 < sentimental_8 or sentimental_7 == sentimental_8 and nome_8 > nome_7:
        aux_nome = nome_7
        aux_custo = custo_7
        aux_sentimental = sentimental_7
        nome_7 = nome_8
        custo_7 = custo_8
        sentimental_7 = sentimental_8
        nome_8 = aux_nome
        custo_8 = aux_custo
        sentimental_8 = aux_sentimental

    if custo_8 < custo_9 or custo_8 == custo_9 and sentimental_8 < sentimental_9 or sentimental_8 == sentimental_9 and nome_9 > nome_8:
        aux_nome = nome_8
        aux_custo = custo_8
        aux_sentimental = sentimental_8
        nome_8 = nome_9
        custo_8 = custo_9
        sentimental_8 = sentimental_9
        nome_9 = aux_nome
        custo_9 = aux_custo
        sentimental_9 = aux_sentimental

    if custo_9 < custo_10 or custo_9 == custo_10 and sentimental_9 < sentimental_10 or sentimental_9 == sentimental_10 and nome_10 > nome_9:
        aux_nome = nome_9
        aux_custo = custo_9
        aux_sentimental = sentimental_9
        nome_9 = nome_10
        custo_9 = custo_10
        sentimental_9 = sentimental_10
        nome_10 = aux_nome
        custo_10 = aux_custo
        sentimental_10 = aux_sentimental

print(f"{nome_1} {nome_2} {nome_3} {nome_4} {nome_5} {nome_6} {nome_7} {nome_8} {nome_9} {nome_10}")
print(f"{custo_1} {custo_2} {custo_3} {custo_4} {custo_5} {custo_6} {custo_7} {custo_8} {custo_9} {custo_10}")
print(f"{sentimental_1} {sentimental_2} {sentimental_3} {sentimental_4} {sentimental_5} {sentimental_6} {sentimental_7} {sentimental_8} {sentimental_9} {sentimental_10}")