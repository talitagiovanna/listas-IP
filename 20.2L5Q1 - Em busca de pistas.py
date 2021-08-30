X = int(input())
Z = int(input())

def GDR(n):
    if n == 1:
        return 1
    return (GDR(n-1)*n)+1


num = GDR(Z)


if num == X:
    print("Achamos mais uma pista! Estamos quase lá")
else:
    print("Ops, ainda vamos demorar um pouco...")
