nome_1 = input()
P = int(input())
nome_2 = input()
S = int(input())
nome_3 = input()
T = int(input())

if (S < P) or (S == P) and (nome_2 < nome_1):
    A = P
    B = nome_1
    P = S
    S = A
    nome_1 = nome_2
    nome_2 = B
if (T < S) or (T == S) and (nome_3 < nome_2):
    C = S
    D = nome_2
    S = T
    T = C
    nome_2 = nome_3
    nome_3 = D
if (S < P) or (S == P) and (nome_2 < nome_1):
    A = P
    B = nome_1
    P = S
    S = A
    nome_1 = nome_2
    nome_2 = B
print(f"{nome_1} {P}\n{nome_2} {S}\n{nome_3} {T}")