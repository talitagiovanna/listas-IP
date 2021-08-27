S = input()
N = int(input())
num = str(N)
A = len(num)
if len(S)<=20:
    if N%A==0:
        B = int(num[0])
        if N%B==0:
            print(f"Bem-vindo ao banquete, {S}")
        else:
            print("E o Rei Gelado!")
    else:
        print("E o Rei Gelado!")